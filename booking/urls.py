from django.urls import include, path
from rest_framework.routers import DefaultRouter

from booking import views

router = DefaultRouter()
router.register("book-room", views.BookingViewSet, basename="book-room")

urlpatterns = [path("", include(router.urls))]
