import datetime

from django.db.models import Q
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from booking.models import Booking


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ("book_start", "book_end", "room", "user")

    def validate(self, attrs):

        book_start = attrs.get("book_start")
        book_end = attrs.get("book_end")

        if book_start >= book_end:
            raise serializers.ValidationError("End date must be bigger than start date")
        if book_start < datetime.datetime.today().date():
            raise serializers.ValidationError("Start date must be today or later")

        booked_room_id: int = attrs.get("room")
        actual_room_bookings = Booking.objects.filter(
            book_end__gte=datetime.datetime.today().date(), room=booked_room_id
        )
        overlapping_bookings = actual_room_bookings.filter(
            Q(book_start__lte=book_end) & Q(book_end__gte=book_start)
        )

        if overlapping_bookings:
            raise serializers.ValidationError(
                "This room is already booked for this peiod"
            )

        return attrs
