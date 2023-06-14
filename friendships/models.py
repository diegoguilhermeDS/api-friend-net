from django.db import models


class StatusChoices(models.TextChoices):
    REQUESTED = "requested"
    ACCEPTED = "accepted"


class Friendship(models.Model):
    user_requesting = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="requesting"
    )
    user_receiving = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="receiving"
    )
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.REQUESTED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)