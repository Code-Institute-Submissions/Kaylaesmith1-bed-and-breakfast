from django.shortcuts import render, reverse, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic, View
from django.views.generic import ListView
from .forms import CustomerForm, MenuItemForm
from .models import Item, MenuItem
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


class Home(generic.TemplateView):
    """Opens to landing page"""
    template_name = "index.html"


class About(generic.TemplateView):
    """Opens About page"""
    template_name = "about.html"


class Booking(generic.TemplateView):
    """Opens Booking page"""
    template_name = "book.html"


def create_customer(request):
    form = CustomerForm()
    return render(request, 'contact_us.html', {'form': form})


class Breakfast(generic.TemplateView):
    """Opens Menu page"""
    template_name = "breakfast.html"


class MenuDetail(generic.TemplateView):
    """Opens to Delete Menu Item page"""
    template_name = "menu/menu_detail.html"


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


# DELETE MENU ITEM - ADMIN LOGIN REQUIRED - this works but doesn't ask if sure
def delete_menu_item(request, item_id):
    """
    Allows superuser to delete menu item.
    """
    food_item = get_object_or_404(Item, id=item_id)
    food_item.delete()
    messages.success(request, 'Menu item deleted successfully')
    return redirect(reverse('breakfast'))


# def delete_menu_item(request, item_id):
#     """
#     Allows superuser to delete menu item.
#     """
#     update = Item.objects.get(id=item_id)
#     context = {'item': update}
#     messages.success(request, 'Menu item deleted successfully')
#     return redirect(reverse('breakfast'))

# def delete_menu_item(request, item_id):
    # """
    # Allows superuser to delete menu item.
    # """
    # item = get_object_or_404(Item, id=item_id)

    # if request.method == "POST":
    #     item.delete()
    #     messages.success(request, "Menu item deleted successfully")
    #     return redirect(reverse("breakfast"))

    # return render(
    #     request,
    #     "menu/menu_detail.html",
    #     {"item": item},

    # )
