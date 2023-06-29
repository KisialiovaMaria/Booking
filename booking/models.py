from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    number = models.IntegerField(unique=True)
    cost_per_day = models.DecimalField(max_digits=7, decimal_places=2)
    beds_numder = models.IntegerField()


class Booking(models.Model):
    book_start = models.DateField()
    book_end = models.DateField()
    room = models.ForeignKey(
        Room,
        on_delete=models.NOT_PROVIDED,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
