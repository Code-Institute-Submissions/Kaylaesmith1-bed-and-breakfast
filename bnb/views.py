from django.shortcuts import render, reverse, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic, View
from django.views.generic import ListView, FormView
from .forms import CustomerForm, MenuItemForm, AvailabilityForm, BookingForm
from .models import Item, MenuItem, Room, Booking
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# IS THIS INCORRECTLY CALLED?
from .availability import check_availability


class Home(generic.TemplateView):
    """Opens to landing page"""
    template_name = "index.html"


class About(generic.TemplateView):
    """Opens About page"""
    template_name = "about.html"


class BookingPage(generic.TemplateView):
    """Opens Booking page"""
    template_name = "book.html"


# class Booking(generic.TemplateView):
#     """Opens Booking page if user is authenticated or asks them to login"""
#     template_name = "bookings.html"


def create_customer(request):
    form = CustomerForm()
    return render(request, 'contact_us.html', {'form': form})


class Breakfast(generic.TemplateView):
    """Opens Menu page"""
    template_name = "breakfast.html"


class MenuDetail(generic.TemplateView):
    """Opens to Delete Menu Item page"""
    template_name = "menu/menu_detail.html"


class BookingDetail(generic.TemplateView):
    """Opens to Delete A Booking page"""
    template_name = "booking_detail.html"

# CAN DELETE THIS?
# class DeleteMenuItem(DeleteView):
#     model = Item
#     template_name = 'menu_detail.html'
#     success_url = reverse_lazy('breakfast')


# MENU ITEMS & CATEGORIES
class FoodListViews(ListView):
    model = Item
    queryset = Item.objects.all().filter(food_type='Meat')
    template_name = 'breakfast.html'


def food_list(request):
    meat_list = Item.objects.filter(food_type=Item.MEAT)
    bread_list = Item.objects.filter(food_type=Item.SAVORY_BREADS)
    pastry_list = Item.objects.filter(food_type=Item.PASTRIES)
    fruit_list = Item.objects.filter(food_type=Item.FRESH_FRUIT)
    vegan_list = Item.objects.filter(food_type=Item.VEGAN_OPTIONS)
    drinks_list = Item.objects.filter(food_type=Item.DRINKS)
    context = {
        'meat_list': meat_list,
        'bread_list': bread_list,
        'pastry_list': pastry_list,
        'fruit_list': fruit_list,
        'vegan_list': vegan_list,
        'drinks_list': drinks_list,
    }
    return render(request, "breakfast.html", context)


# ADD MENU ITEM - ADMIN LOGIN REQUIRED
def add_menu_item(request):
    """
    Allows superuser to add menu item
    """

    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New menu item added successfully')
            return redirect(reverse('breakfast'))
        else:
            messages.error(
                request,
                'An error occurred, please try again')
    else:
        form = MenuItemForm()

    template = 'menu/add_menu_item.html'
    context = {
        'form': form
    }

    return render(request, template, context)


# EDIT MENU ITEM - ADMIN LOGIN REQUIRED
def update_menu_item(request, item_id):
    """
    Allows superuser to edit menu item
    """
    update = Item.objects.get(id=item_id)
    form = MenuItemForm(instance=update)

    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=update)
        if form.is_valid():
            form.save()
            messages.success(request, 'New menu item added successfully')
            return redirect(reverse('breakfast'))
        else:
            messages.error(
                request,
                'An error occurred, please try again')

    context = {'form': form}
    template = 'menu/edit_menu_item.html'
    return render(request, template, context)


# DELETE MENU ITEM - ADMIN LOGIN REQUIRED
def delete_menu_item(request, item_id):
    """
    Allows superuser to delete menu item.
    """
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        item.delete()
        messages.success(request, "Menu item deleted successfully")
        return redirect(reverse("my_bookings"))

    return render(
        request,
        "booking_detail.html",
        {"item": item},

    )


# BOOKINGS - video at 10:30 creates .html pages for these two views (is this necessary?)
class RoomList(ListView):
    """Opens Room List page"""
    model = Room
    template_name = "room_list.html"


# BOOKING FORM TEST
class BookingList(ListView):
    """Opens Booking List page"""
    model = Booking
    template_name = "booking_list.html"


# USERS LIST OF BOOKINGS TO EDIT / DELETE
class BookingListView(generic.DetailView):
    """
    This is the view that will bring up the
    list of bookings for a particular users
    so that they can be edited or deleted
    """

    template_name = 'my_bookings.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)

            return render(request, 'my_bookings.html', {
                'bookings': bookings
            }
            )
        else:
            return redirect('account_login')


# BOOKING FORM FOR AUTHENTICATED / ADMIN USERS
class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = "bookings.html"

    def form_vaild(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(

                user=request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse('Your room has been booked!')
        else:
            return HttpResponse('This room is unavailable at the moment.')


# EDIT YOUR BOOKING - AUTHENTICATED / ADMIN USERS ONLY
# SOURCE: https://github.com/Martiless/nondairy-godmother
def edit_bookings(request, booking_id):
    """
    When a user is on the My Bookings page
    which can only be accessed if you are
    logged in, they can click on the edit button.
    This will bring them to a new page, where the booking
    they wish to edit, located using the booking id,
    appears, prepopulated with the current information.
    Once the user clicks on the submit changes button
    they will be redirected to the home page and a
    confimation message will appear.
    """

    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(instance=booking)

        if booking.user == request.user:
            if request.method == 'POST':
                form = BookingForm(data=request.POST, instance=booking)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your booking has been updated')
                    return redirect('my_bookings')

    return render(request, 'edit_bookings.html', {
        'form': form
        })


# DELETE YOUR BOOKING - AUTHENTICATED / ADMIN USERS ONLY
# SOURCE: https://github.com/Martiless/nondairy-godmother
def delete_booking(request, booking_id):
    """
    When a user is on the My Bookings page
    which can only be accessed if you are
    logged in, they can click on the cancel booking
    button. This will cancel the booking using its
    booking id, redirect the user back to the home page and
    pop up a confimation message will appear.
    """
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)

        if booking.user == request.user:
            booking.delete()
            messages.success(request, 'Booking deleted successfully')
            return redirect('/')


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking has been deleted successfully")
        return redirect(reverse("my_bookings"))
    
    return render(
        request,
        "booking_detail.html",
        {"booking": booking},

    )
