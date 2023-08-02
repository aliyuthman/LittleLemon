from django.db import models

# Create your models here.


class Menu(models.Model):
    """Model definition for Menu."""

    # id = models.IntegerField(primary_key=True, max_length=5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        """Unicode representation of Menu."""
        pass


class Booking(models.Model):
    """Model definition for Booking."""
    # id = models.IntegerField(primary_key=True, max_length=11)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(max_length=6)
    booking_date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        """Unicode representation of Booking."""
        pass
