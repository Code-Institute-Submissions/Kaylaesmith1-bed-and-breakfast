from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings


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
        ('food_type'),
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


# ADD NEW CATEGORY TO DJANGO DATABASE
class MenuItem(models.Model):
    item_name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)


# CHECK AVAILABILITY
# class Availability(models.Model):
#     ROOM_CATEGORIES = (
#         ('Master Bedroom', 'Master Bedroom'),
#         ('Queen Bedroom', 'Queen Bedroom'),
#     )
#     room_category = models.CharField(max_length=100, choices=ROOM_CATEGORIES)
#     check_in = models.DateField()
#     check_out = models.DateField()


# BOOK A ROOM
class Room(models.Model):
    ROOM_CATEGORIES = (
        ('Master Bedroom', 'Master Bedroom'),
        ('Queen Bedroom', 'Queen Bedroom'),
    )
    # WILL ONLY EVER HAVE 2 ROOMS AVAILABLE AT ANY GIVEN TIME
    number = models.IntegerField()
    category = models.CharField(max_length=50, choices=ROOM_CATEGORIES, blank=True, null=True)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} bed/s for {self.capacity} people.'


# MAYBE DELETE - TROUBLESHOOTING
class Booking(models.Model):
    """
    It uses the User Foreign Key so that each book will be associated with a
    specific user. User is authenticated but doesn't have to be Admin.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'


# class Booking(models.Model):
#     """
#     Model to be used in the forms.py and views.py for the booking form.
#     It uses the User Foreign Key so that each book will be associated with a
#     specific user.
#     The rest of the information is saved for the booking
#     """

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=60, null=True, blank=True)
#     email_address = models.EmailField(null=True, blank=True)
 
#     date = models.DateField()
    
#     def __str__(self):
#         return self.name
