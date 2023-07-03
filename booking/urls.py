from django.urls import include, path
from rest_framework.routers import DefaultRouter

from booking import views

router = DefaultRouter()
router.register("book-room", views.BookingViewSet, basename="book-room")
router.register("book", views.CancelBookViewSet, basename="book")
router.register("rooms", views.RoomsViewSet, basename="rooms")
router.register(
    "search-free-rooms", views.SearchFreeRoomsViewSet, basename="search-free-rooms"
)

urlpatterns = [
    path("", include(router.urls)),
]
