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


# MENU ITEMS & CATEGORIES
class FoodListViews(ListView):
    model = Item
    queryset = Item.objects.all().filter(food_type='Meat')
    # queryset = Item.objects.order_by('food_type')
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


def add_menu_item(request):
    form = MenuItemForm()
    return render(request, 'menu/add_menu_item.html', {'form': form})



# def contactView(request):
#     if request.method == "GET":
#         form = CustomerForm()
#     else:
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data["subject"]
#             from_email = form.cleaned_data["from_email"]
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ["kaylaesmith1@gmail.com"])
#             except BadHeaderError:
#                 return HttpResponse("Invalid header found.")
#             return redirect("success")
#     return render(request, 'contact_us.html', {'form': form})

# def successView(request):
#     return HttpResponse("Success! Thank you for your message.")


# ADMIN LOGINS REQUIRED
@login_required
def add_menu_item(request):
    """
    Allows superuser to add menu item
    """

    if not request.user.is_superuser:
        messages.error(request, 'Please log in as an admin to add menu items.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New menu item added successfully')
            return redirect(reverse('breakfast'))
        else:
            messages.error(
                request,
                'An error occurred, please make sure the form is valid')
    else:
        form = MenuItemForm()

    template = 'menu/add_menu_item.html'
    context = {
        'form': form
    }

    return render(request, template, context)

    
# @login_required
# def edit_menu_item(request):
#     """
#     Allows superuser to edit a menu item
#     """

#     if not request.user.is_superuser:
#         messages.error(request, 'Please log in as an admin to edit menu items.')
#         return redirect(reverse('home'))

#     if request.method == 'POST':
#         form = MenuItemForm(request.POST, request.FILES, instance=menu)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Menu item edited successfully')
#             return redirect(reverse('menu_detail'))
#         else:
#             messages.error(
#                 request,
#                 'An error occurred, please make sure the form is valid')
#     else:
#         form = MenuItemForm(instance=menu)
#         messages.info(request, f'You are editing {menu.name}')

#     template = 'menu/edit_menu_item.html'
#     context = {
#         'form': form,
#         'menu': menu
#     }

#     return render(request, template, context)


# @login_required
# def delete_menu_item(request):
#     """
#     Allows superuser to delete a menu item.
#     """

#     if not request.user.is_superuser:
#         messages.error(request, 'Log in as an admin to delete menu items.')
#         return redirect(reverse('home'))
