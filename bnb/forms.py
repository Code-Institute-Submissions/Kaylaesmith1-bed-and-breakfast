from django import forms
from .models import Customer, Menu, Item
# from .models import Customer, Menu, MenuItem


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


# DELETE THIS BELOW
# class ItemForm(forms.ModelForm):

#     class Meta:
#         model = AddItem
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(). __init__(*args, **kwargs)
