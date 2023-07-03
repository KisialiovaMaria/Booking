from django.db.models import Q
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import mixins, status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from booking import permissions
from booking.models import Booking, Room
from booking.serializers import BookingSerializer, RoomSerializer


class BookingViewSet(
    permissions.PermissionPolicyMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = (IsAuthenticated,)
    permission_classes = {
        "create": (IsAuthenticated,),
        "list": (IsAuthenticated,),
        "destroy": (
            IsAuthenticated,
            permissions.IsBookedPerson | permissions.IsSuperuser,
        ),
    }

    def create(self, request, *args, **kwargs):
        request.data["user"]: int = request.user.id
        serializer: BookingSerializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        self.queryset = Booking.objects.filter(user=request.user)
        response = super().list(request, *args, **kwargs)

        return response


class RoomsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = RoomSerializer
    permission_classes = ()
    queryset = Room.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["cost_per_day", "beds_numder"]
    ordering_fields = "__all__"


class SearchFreeRoomsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = RoomSerializer
    permission_classes = ()

    def get_queryset(self):
        book_start: str = self.request.query_params.get("start_date")
        book_end: str = self.request.query_params.get("end_date")

        if book_end and book_start:
            non_booking_rooms = Room.objects.exclude(
                Q(booking__book_start__lte=book_end)
                & Q(booking__book_end__gte=book_start)
            )

        return non_booking_rooms
