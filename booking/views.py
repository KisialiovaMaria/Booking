import operator

import django_filters
from django.contrib.auth.models import User
from django.db.models import Count, Q, QuerySet
from django_filters import DateFilter
from django_filters.rest_framework import FilterSet
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import mixins, status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from booking import permissions
from booking.models import Booking, Room
from booking.serializers import (
    BookingSerializer,
    RoomSerializer,
    UserRegistrySerializer,
)


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
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ("cost_per_day", "beds_numder")
    ordering_fields = "__all__"


class FreeRoomsFilter(django_filters.FilterSet):
    start_date = DateFilter(
        field_name="booking__book_end", lookup_expr=("lte"), required=True
    )
    end_date = DateFilter(
        field_name="booking__book_start", lookup_expr=("gte"), required=True
    )

    class Meta:
        model = Room
        fields = ["start_date", "end_date"]


class SearchFreeRoomsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = RoomSerializer
    permission_classes = ()
    queryset = Room.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = FreeRoomsFilter


class RegistryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrySerializer

    def create(self, request, *args, **kwargs):
        serializer: UserRegistrySerializer = UserRegistrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
