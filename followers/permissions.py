from urllib.request import Request
from django.views import View
from rest_framework import permissions


class FollowersPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated