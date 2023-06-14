from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.db.models import Q
from rest_framework import generics
from rest_framework.views import Response, status, APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Like
from posts.models import Post
from users.models import User
from friendships.models import Friendship
from followers.models import Follower
from .serializers import LikeSerializer


class LikeView(generics.ListCreateAPIView, generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "post_id"

    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs["post_id"])
        if (
            model_to_dict(post)["published_by"] == self.request.user.id
            or model_to_dict(post)["private"] is False
        ):
            return Like.objects.filter(post_id=post)

        user = User.objects.get(pk=model_to_dict(post)["published_by"])
        friend = Friendship.objects.filter(user_receiving=user).first()
        follow = Follower.objects.filter(user_followed=user).first()
        if friend or follow:
            return Like.objects.filter(post_id=post)
        return get_object_or_404(Like, pk=-1)

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs["post_id"])
        user = User.objects.get(pk=model_to_dict(post)["published_by"])
        friend = Friendship.objects.filter(user_receiving=user).first()
        follow = Follower.objects.filter(user_followed=user).first()
        if (
            model_to_dict(post)["published_by"] == self.request.user.id
            or model_to_dict(post)["private"] is False
        ):
            like, created = Like.objects.get_or_create(
                user_id=request.user, post_id=post
            )
            if created:
                like_serialized = LikeSerializer(like)
                return Response(like_serialized.data, status=status.HTTP_201_CREATED)

            return Response(
                data={"message": "Post already liked"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        elif friend or follow:
            like, created = Like.objects.get_or_create(
                user_id=request.user, post_id=post
            )
            if created:
                like_serialized = LikeSerializer(like)
                return Response(like_serialized.data, status=status.HTTP_201_CREATED)

        return Response(
            data={"detail": f"Not authorized"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, *args, **kwargs):
        user = request.user
        post = get_object_or_404(Post, pk=self.kwargs["post_id"])
        try:
            post_like = Like.objects.get(Q(user_id=user) & Q(post_id=post))
            post_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Like.DoesNotExist:
            return Response(
                data={
                    "detail": f"The user {user.__dict__['username']} didn't liked this post yet"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
