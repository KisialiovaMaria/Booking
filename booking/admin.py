from django.contrib import admin
from django.contrib.auth.models import Group, User

from booking.models import Booking, Room

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "is_superuser", "password")

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "cost_per_day",
        "beds_numder",
    )
    search_fields = (
        "number",
        "cost_per_day",
        "beds_numder",
    )
    list_filter = ("beds_numder",)


@admin.register(Booking)
class RoomAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    list_display = (
        "id",
        "book_start",
        "book_end",
        "room",
        "user",
    )
