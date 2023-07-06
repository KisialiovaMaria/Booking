from django.urls import include, path
from rest_framework.routers import DefaultRouter

from booking import views

router = DefaultRouter()
router.register("room-bookings", views.BookingViewSet, basename="room-bookings")
router.register("rooms", views.RoomsViewSet, basename="rooms")
router.register("free-rooms", views.SearchFreeRoomsViewSet, basename="free-rooms")
router.register("registry", views.RegistryViewSet, basename="registry")

urlpatterns = [
    path("", include(router.urls)),
]
