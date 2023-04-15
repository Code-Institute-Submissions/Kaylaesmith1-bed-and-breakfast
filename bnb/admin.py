from django.contrib import admin
from .models import Menu, Item


class MenuAdmin(admin.ModelAdmin):
    """
    Add other menu items to the Breakfast page
    """

    list_display = (
        'category',
        'name',
        'description',
    )


admin.site.register(Menu, MenuAdmin)


# @admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')


admin.site.register(Item, ItemAdmin)
