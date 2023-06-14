from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Comment
from followers.models import Follower
from friendships.models import Friendship
from posts.models import Post
from users.models import User
from django.db.models import Q
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404


class CommentPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        post = get_object_or_404(
            Post, pk=request.parser_context.get("kwargs")["post_id"]
        )
        published_by_id = model_to_dict(post)["published_by"]
        commenting_user_id = request.user.id

        if published_by_id == commenting_user_id and request.user.is_authenticated:
            return True

        user_posted = User.objects.get(pk=published_by_id)
        user_commenting = User.objects.get(pk=commenting_user_id)

        user_friend_requested = Friendship.objects.filter(
            user_receiving=user_posted, user_requesting=user_commenting
        )
        user_friend_received = Friendship.objects.filter(
            user_receiving=user_commenting, user_requesting=user_posted
        )
        if len(user_friend_requested) > 0 or len(user_friend_received) > 0:
            if len(user_friend_requested) > 0:
                return (
                    model_to_dict(user_friend_requested.first())["status"] == "accepted"
                )

            else:
                return (
                    model_to_dict(user_friend_received.first())["status"] == "accepted"
                )

        return False


class CommentObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Comment):
        return (
            request.user.is_authenticated
            and request.user.id == model_to_dict(obj)["user_commented"]
        )
