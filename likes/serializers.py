from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "user_id", "post_id", "created_at"]
        read_only_fields = ["created_at", "user_id", "post_id"]
        write_only_fields = ["user_id", "post_id"]
