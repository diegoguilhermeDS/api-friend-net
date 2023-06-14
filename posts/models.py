from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    private = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )
