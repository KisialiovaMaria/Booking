from django.urls import include, path
from rest_framework.routers import DefaultRouter

from booking import views

router = DefaultRouter()
router.register("room-bookings", views.BookingViewSet, basename="room-bookings")
router.register("rooms", views.RoomsViewSet, basename="rooms")
router.register("free-rooms", views.SearchFreeRoomsViewSet, basename="free-rooms")

urlpatterns = [
    path("", include(router.urls)),
]
