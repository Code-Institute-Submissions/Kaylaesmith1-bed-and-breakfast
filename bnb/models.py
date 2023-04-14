from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# CONTACT FORM
class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    message = models.TextField(max_length=350, blank=True)

    def __str__(self):
        return str(self.title)


# ADD MENU ITEM AS ADMIN THROUGH DJANGO
class Menu(models.Model):
    """
    Menu Item
    """
    category = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=350)

    def __str__(self):
        return self.name


# MENU ITEM CATEGORIES
class Item(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(max_length=250)

    MEAT = "Meat"
    SAVORY_BREADS = "Bread"
    PASTRIES = "Pastry"
    FRESH_FRUIT = "Fruit"
    VEGAN_OPTIONS = "Vegan"
    DRINKS = "Drinks"

    FOOD_TYPE = [
        (MEAT, "Meat"),
        (SAVORY_BREADS, "Bread"),
        (PASTRIES, "Pastry"),
        (FRESH_FRUIT, "Fruit"),
        (VEGAN_OPTIONS, 'Vegan'),
        (DRINKS, 'Drinks'),
    ]
    food_type = models.CharField(
        ('Food type'),
        max_length=25,
        choices=FOOD_TYPE,
        default="Meat"
        )

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
