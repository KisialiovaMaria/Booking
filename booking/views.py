import generics as generics
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import mixins, status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from booking import permissions
from booking.models import Booking, Room
from booking.serializers import BookingSerializer, RoomSerializer


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
    permission_classes = (IsAuthenticated, permissions.IsBookedPerson)


class RoomsViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = ()
    queryset = Room.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["cost_per_day", "beds_numder"]
    ordering_fields = "__all__"
