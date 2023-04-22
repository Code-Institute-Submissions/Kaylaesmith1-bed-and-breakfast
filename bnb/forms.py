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


# BOOKING (AVAILABILITY) FORM - Delete this?
# class AvailabilityForm(forms.Form):
#     ROOM_CATEGORIES = (
#         ('Master Bedroom', 'Master Bedroom'),
#         ('Second Bedroom', 'Second Bedroom'),
#     )
#     room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
#     check_in = forms.DateTimeField(required=True, input_formats=['%m/%d/%y', ])
#     check_out = forms.DateTimeField(required=True, input_formats=['%m/%d/%y', ])


# SELECT DATE FROM CALENDAR BUTTON
class DateInput(forms.DateInput):
    """
    Calendar widget to choose check-in / check-out dates
    """
    input_type = 'date'


# BOOKING FORM
class BookingForm(forms.ModelForm):
    """
    This form is connected with the view
    in order to provide users with the neccessary
    fields for making a booking
    It also provides the labels and placeholder
    text for each field, as wells as the widgets
    and handles validation where required.
    """

    class Meta:
        model = Booking
        fields = '__all__'
        # calendar widget not working
        widgets = {
            'date': forms.DateInput
        }



            # ROOM_CATEGORIES = (
    #     ('Master Bedroom', 'Master Bedroom'),
    #     ('Second Bedroom', 'Second Bedroom'),
    # )
    # name = forms.CharField(label='Booking Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'Booking Name'}),)
    # room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True, widget=forms.TextInput(attrs={'placeholder': 'Room Choice'}),)
    # name = forms.CharField(
    #     label='Booking Name',
    #     required=True,
    #     widget=forms.TextInput(attrs={'placeholder': 'Booking Name'}),
    # )

    # email_address = forms.EmailField(
    #     label='Email Address',
    #     required=True,
    #     widget=forms.TextInput(attrs={'placeholder': 'Email Address'}),
    # )
    # check_in = forms.DateTimeField(required=True, input_formats=['%m/%d/%y', ])
    # check_out = forms.DateTimeField(required=True, input_formats=['%m/%d/%y', ])

# TEST BOOKING FORM
# class BookRoomFormTest(forms.ModelForm):
#     class Meta:
#         model = BookRoomTest
#         fields = ['name', 'email', 'check_in', 'check_out', 'room_type']
#         widgets = {
#             'date': DateInput()
#         }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     check_in = cleaned_data.get('check_in')
    #     check_out = cleaned_data.get('check_out')
    #     room_type = cleaned_data.get('room_type')
    #     if check_in and check_out and room_type:
    #         bookings = BookRoomTest.objects.filter(room_type=room_type)
    #         for booking in bookings:
    #             if booking.check_in <= check_out and check_in <= booking.check_out:
    #                 messages.error(request, 'An error occurred, please try again')
