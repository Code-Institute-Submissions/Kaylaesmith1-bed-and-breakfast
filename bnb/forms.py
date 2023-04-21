from django import forms
from .models import Customer, Menu, Item, Booking


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
    check_in = forms.DateTimeField(required=True, input_formats=['%m/%d/%y %H:%M', ])
    check_out = forms.DateTimeField(required=True, input_formats=['%m/%d/%y %H:%M', ])


# SELECT DATE FROM CALENDAR BUTTON - DO WE NEED??
# class DateInput(forms.DateInput):
#     """
#     This class provides a widget for use in the
#     booking form. It provides a calendar for users
#     to pick the booking date from
#     """
#     input_type = 'date'


# BOOKING FORM - delete?
# class BookingForm(forms.ModelForm):
#     """
#     This form is connected with the view
#     in order to provide users with the neccessary
#     fields for making a booking
#     It also provides the labels and placeholder
#     text for each field, as wells as the widgets
#     and handles validation where required.
#     """
#     ROOM_CATEGORIES = (
#         ('MBD', 'Master Bedroom'),
#         ('BD2', 'Second Bedroom'),
# )
#     name = forms.CharField(label='Booking Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'Booking Name'}),)
#     room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True, widget=forms.TextInput(attrs={'placeholder': 'Room Choice'}),)
#     check_in = forms.DateTimeField(required=True, input_formats=["%d-%m-%yT%H:%M", ])
#     check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])

#     class Meta:
#         """Defines which model to pull the
#         fields from"""
#         model = Booking
#         fields = '__all__'
#         exclude = ('user', )
#         widgets = {
#             'date': DateInput()
#         }
