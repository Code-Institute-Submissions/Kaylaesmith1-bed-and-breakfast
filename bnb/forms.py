from django import forms
from .models import Customer, Menu, Item, Booking


class CustomerForm(forms.ModelForm):
    """ Customer Contact Form on Contact Us page
    Linked to Email JS
    """

    class Meta:
        model = Customer
        fields = "__all__"


class MenuItemForm(forms.ModelForm):
    """Add menu item from live site to Django DB"""

    class Meta:
        model = Item
        fields = ['name', 'description', 'food_type']

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)


class BookingForm(forms.ModelForm):
    """Booking Form"""

    class Meta:
        model = Booking
        fields = '__all__'
        # exclude = ('user',)
        # fields = ['room', 'check_in', 'check_out']
