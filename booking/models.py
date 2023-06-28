from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    number = models.IntegerField(max_length=4, unique=True)
    cost_per_day = models.DecimalField(max_digits=7, decimal_places=2)
    beds_numder = models.IntegerField(max_length=3)

class Booking(models.Model):
    book_start = models.DateTimeField()
    book_end = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.NOT_PROVIDED, )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)