from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from booking.models import Booking, Room
from booking.permissions import IsBookedPerson
from booking.serializers import BookingSerializer


class BookingViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = BookingSerializer
    queryset = Room.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        serializer: BookingSerializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class CancelBookViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = (IsAuthenticated, IsBookedPerson)
