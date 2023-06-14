from django.db import models


class Follower(models.Model):
    user_following = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="following"
    )
    user_followed = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="followed"
    )
    created_at = models.DateTimeField(auto_now_add=True)
