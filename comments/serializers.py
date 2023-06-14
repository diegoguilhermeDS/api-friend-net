from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "created_at", "user_commented", "commented_post"]
        read_only_fields = ["id", "created_at", "user_commented", "commented_post"]

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
