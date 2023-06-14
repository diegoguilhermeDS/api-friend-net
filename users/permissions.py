from rest_framework import permissions
from rest_framework.views import View
from .models import User


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_authenticated and obj == request.user


class IsGetAuthenticatedRequest(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_authenticated
        return super().has_permission(request, view)
