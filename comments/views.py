from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Comment
from .serializers import CommentSerializer
from .permissions import CommentPermission, CommentObjectPermission
from posts.models import Post
from django.shortcuts import get_object_or_404

# Create your views here.


class CommentView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CommentPermission]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "post_id"

    def perform_create(self, serializer):
        user_current = self.request.user
        post = get_object_or_404(Post, pk=self.kwargs["post_id"])

        return serializer.save(user_commented=user_current, commented_post=post)


class CommentDetailView(generics.DestroyAPIView, generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CommentObjectPermission]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "pk"
