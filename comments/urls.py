from django.urls import path
from . import views

urlpatterns = [
    path("posts/<int:post_id>/comments/", views.CommentView.as_view()),
    path("posts/comments/<int:pk>/", views.CommentDetailView.as_view()),
]
