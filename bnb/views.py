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


def create_customer(request):
    form = CustomerForm()
    return render(request, 'contact_us.html', {'form': form})


class Breakfast(generic.TemplateView):
    """Opens Menu page"""
    template_name = "breakfast.html"


class MenuDetail(generic.TemplateView):
    """Opens to Delete Menu Item page"""
    template_name = "menu/menu_detail.html"


# class EditMenuDetail(generic.TemplateView):
#     """Opens to Edit Menu Item page"""
#     template_name = "menu/edit_menu_item.html"


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


# ADMIN LOGINS REQUIRED TO ADD, EDIT & DELETE MENU ITEMS

# ADD MENU ITEM
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


# EDIT MENU ITEM
def edit_menu_item(request, item_id):
    """
    Allows superuser to edit a menu item
    """

    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        # form = MenuItemForm(request.POST, request.FILES, instance=item_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu item edited successfully')
            return redirect(reverse('breakfast'))
        else:
            messages.error(
                request,
                'An error occurred, please try again')
    # else:
    #     form = MenuItemForm(instance=item_id)
    #     messages.info(request, f'You are editing {Item.name}')

    template = 'menu/edit_menu_item.html'
    context = {
        'form': form,
        'item_id': item_id
    }

    return render(request, template, context)


# DELETE MENU ITEM
def delete_menu_item(request, item_id):
    """
    Allows superuser to delete menu item.
    """

    food_item = get_object_or_404(Item, id=item_id)
    food_item.delete()
    # return redirect(reverse('menu_detail', args=[item.id]))
    messages.success(request, 'Menu item deleted successfully')
    return redirect(reverse('breakfast'))
