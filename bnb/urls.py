from . import views
from django.urls import path
from .views import create_customer, food_list, add_menu_item, update_menu_item, delete_menu_item, delete_booking

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),

    # DELETE THIS URL AND TAKE CSS TO my_bookings PAGE
    path('book/', views.BookingPage.as_view(), name='book'),

    path('contact/', create_customer, name='contact_us'),
    path('breakfast/', food_list, name='breakfast'),
    path('add/', add_menu_item, name='add_menu_item'),
    path('edit/<item_id>/', update_menu_item, name='edit_menu_item'),
    path('menu/', views.MenuDetail.as_view(), name='menu_detail'),
    path('delete/<item_id>/', delete_menu_item, name='delete_item'),

    path('bookings/', views.BookingView.as_view(), name='bookings'),

    path('my_bookings/', views.BookingListView.as_view(), name='my_bookings'),
    path('edit_bookings/<booking_id>', views.edit_bookings, name='edit_bookings'),
    path('booking_detail/', views.BookingDetail.as_view(), name='booking_detail'),
    path('delete_booking/<booking_id>', delete_booking, name='delete_booking'),

    

    path('room_list/', views.RoomList.as_view(), name='room_list'),
    path('booking_list/', views.BookingList.as_view(), name='booking_list'),
    ]
