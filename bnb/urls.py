from . import views
from django.urls import path
from .views import create_customer, food_list, add_menu_item, update_menu_item, delete_menu_item

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', create_customer, name='contact_us'),
    path('breakfast/', food_list, name='breakfast'),
    path('add/', add_menu_item, name='add_menu_item'),
    path('edit/<item_id>/', update_menu_item, name='edit_menu_item'),
    path('menu/', views.MenuDetail.as_view(), name='menu_detail'),
    path('delete/<item_id>/', delete_menu_item, name='menu_detail'),
]
