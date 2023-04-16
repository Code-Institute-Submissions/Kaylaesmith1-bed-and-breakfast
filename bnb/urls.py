from . import views
from django.urls import path
from .views import create_customer, food_list, add_menu_item

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('contact/', views.Contact.as_view(), name='contact_us'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', create_customer, name='contact_us'),
    # path('breakfast/', views.Breakfast.as_view(), name='breakfast'),
    path('breakfast/', food_list, name='breakfast'),
    # path('add/', views.add_menu_item, name="add_menu_item"),
    path('add/', add_menu_item, name='add_menu_item'),
    # path('myaccount/', views.MyAccount.as_view(), name='my_account'),
]
