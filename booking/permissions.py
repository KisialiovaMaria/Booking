from rest_framework import permissions


class PermissionPolicyMixin:
    def get_permissions(self):
        action_permission_classes = self.permission_classes.get(self.action, [])
        return [permission() for permission in action_permission_classes]


class IsBookedPerson(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
