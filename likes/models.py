from django.db import models


# Create your models here.
class Like(models.Model):
    user_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="liked_by_user_id"
    )
    post_id = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="post_likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
