from django.urls import path
from .views import FollowersDetailView, FollowersIFollowView, FollowersMyFollowersView

urlpatterns = [
    path("followers/<int:pk>/", FollowersDetailView.as_view()),
    path("followers/i-follow/", FollowersIFollowView.as_view()),
    path("followers/my-followers/", FollowersMyFollowersView.as_view()),
]
