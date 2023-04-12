from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=350, blank=True)

    def __str__(self):
        return str(self.title)


class Menu(models.Model):
    """
    Menu Item
    """

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=350)

    def __str__(self):
        return self.name
