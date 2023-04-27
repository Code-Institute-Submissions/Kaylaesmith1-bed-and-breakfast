from django.shortcuts import render, reverse, redirect, get_object_or_404, get_list_or_404  # noqa
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic, View
from django.views.generic import ListView, FormView
from .forms import CustomerForm, MenuItemForm, BookingForm
from .models import Item, MenuItem, Room, Booking
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


class Home(generic.TemplateView):
    """Opens to landing page"""
    template_name = "index.html"


class About(generic.TemplateView):
    """Opens About page"""
    template_name = "about.html"


def create_customer(request):
    """Customer Contact Form"""
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


class FoodListViews(ListView):
    """Menu Items& Food Categories"""
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


@login_required
def add_menu_item(request):
    """Allows superuser to ADD menu item"""

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


@login_required
def update_menu_item(request, item_id):
    """Allows superuser to EDIT menu item"""
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


@login_required
def delete_menu_item(request, item_id):
    """Allows superuser to DELETE menu item"""
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        item.delete()
        messages.success(request, "Menu item deleted successfully")
        return redirect(reverse("breakfast"))

    return render(
        request,
        "menu/menu_detail.html",
        {"item": item},

    )


class BookingListView(generic.DetailView):
    """
    This is the view that will bring up the
    list of bookings for a particular users
    so that they can be edited or deleted
    """

    template_name = 'my_bookings.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print((Booking.objects.all()))
            bookings = Booking.objects.filter(user=request.user)

            return render(request, 'my_bookings.html', {
                'bookings': bookings
            }
            )
        else:
            return redirect('account_login')


@login_required
def add_booking(request):
    """
    Allows authenticated user to add booking
    """

    if request.method == 'POST':

        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Booking added successfully')
            return redirect(reverse('my_bookings'))
        else:
            messages.error(
                request,
                'An error occurred, please try again')
    else:
        form = BookingForm()

    template = 'bookings.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_bookings(request, booking_id):
    """
    Authenticated users can edit their own bookings.
    If they choose to edit a booking, they can click
    the 'edit' button, which will take them to a page
    with their booking information, prepopulated with
    the current information. They can change the information
    and update the changes.  A confirmation will appear and
    they'll be redirected to the My Bookings page.
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


@login_required
def delete_booking(request, booking_id):
    """
    Authenticated users can delete their own bookings
    if they choose. If they click the 'delete' button
    they will be taken to a page asking if they're
    sure they want to delete that booking. If they click
    'cancel' they'll be returned to the My Bookings
    page. If they click 'delete' the booking will
    be deleted permanently.
    """
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
