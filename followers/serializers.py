from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = [
            "id",
            "user_following_id",
            "user_followed_id",
            "created_at"
        ]
