from django.db import models

# Create your models here.


class Comment(models.Model):
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    user_commented = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_comments"
    )
    commented_post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="post_comments"
    )
