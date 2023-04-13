from django.contrib import admin
from .models import Menu


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
