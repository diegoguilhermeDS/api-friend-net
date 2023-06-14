from rest_framework import serializers
from .models import Post
from comments.models import Comment
from likes.models import Like


class PostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "created_at", "user_commented", "commented_post"]
        read_only_fields = ["id", "created_at", "user_commented"]
        extra_kwargs = {"commented_post": {"write_only": True, "required": False}}


class PostLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "post_id", "user_id", "created_at"]
        extra_kwargs = {"post_id": {"write_only": True, "required": False}}


class PostSerializer(serializers.ModelSerializer):
    post_comments = PostCommentsSerializer(many=True, read_only=True)
    post_likes = PostLikesSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "description",
            "private",
            "created_at",
            "published_by",
            "post_comments",
            "post_likes",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "published_by",
            "post_comments",
            "post_likes",
        ]
