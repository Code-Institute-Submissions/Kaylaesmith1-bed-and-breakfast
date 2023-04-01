from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact_us'),
    # path('myaccount/', views.MyAccount.as_view(), name='my_account'),
]
