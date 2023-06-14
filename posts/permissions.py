from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Post


class PostsPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated


class PostObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Post):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.published_by


class TimelinePermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated
