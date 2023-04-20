from django import forms
from .models import Customer, Menu, Item


# CUSTOMER CONTACT FORM ON CONTACT US PAGE - LINKED TO EMAIL JS
class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = "__all__"


# ADD MENU ITEM FROM LIVE SITE TO DJANGO DB
class MenuItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'description', 'food_type']

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)


# BOOKING (AVAILABILITY) FORM - user must be logged in
class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('MBD', 'Master Bedroom'),
        ('BD2', 'Second Bedroom'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
