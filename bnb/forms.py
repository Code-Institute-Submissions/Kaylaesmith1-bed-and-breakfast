from django import forms
from .models import Customer, Menu, Item, Availability


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


class AvailabilityForm(forms.Form):

    class Meta:
        model = Availability
        fields = ['room_category', 'check_in', 'check_out']

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)


# BOOKING (AVAILABILITY) FORM - user must be logged in
# class AvailabilityForm(forms.Form):
#     ROOM_CATEGORIES = (
#         ('MBD', 'Master Bedroom'),
#         ('BD2', 'Second Bedroom'),
#     )
#     room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
#     check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
#     check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])


# SELECT DATE FROM CALENDAR BUTTON - DO WE NEED??
# class DateInput(forms.DateInput):
#     """
#     This class provides a widget for use in the
#     booking form. It provides a calendar for users
#     to pick the booking date from
#     """
#     input_type = 'date'
