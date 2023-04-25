from . import views
from django.urls import path
from .views import create_customer, food_list, add_menu_item, update_menu_item, delete_menu_item, delete_booking, add_booking

urlpatterns = [
    # OPEN NAV BAR PAGES
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', create_customer, name='contact_us'),
    path('breakfast/', food_list, name='breakfast'),

    # ADD / EDIT / DELETE MENU ITEMS
    path('add/', add_menu_item, name='add_menu_item'),
    path('edit/<item_id>/', update_menu_item, name='edit_menu_item'),
    path('menu/', views.MenuDetail.as_view(), name='menu_detail'),
    path('delete/<item_id>/', delete_menu_item, name='delete_item'),

    # ADD / EDIT / DELETE A BOOKING
    path('bookings/', add_booking, name='bookings'),
    path('my_bookings/', views.BookingListView.as_view(), name='my_bookings'),
    path('edit_bookings/<booking_id>', views.edit_bookings, name='edit_bookings'),
    path('booking_detail/', views.BookingDetail.as_view(), name='booking_detail'),
    path('delete_booking/<booking_id>', delete_booking, name='delete_booking'),
    ]
