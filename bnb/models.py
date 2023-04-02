from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)
