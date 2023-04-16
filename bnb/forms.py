from django import forms
from .models import Customer, Menu


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = "__all__"


# class MenuItemForm(forms.ModelForm):

#     class Meta:
#         model = Menu
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(). __init__(*args, **kwargs)
