from django.urls import path
from .views import FriendshipsDetailView, FriendshipsReceivedView, FriendshipsRequestedView, FriendshipsView

urlpatterns = [
    path("friendships/", FriendshipsView.as_view()),
    path("friendships/<int:pk>/", FriendshipsDetailView.as_view()),
    path("friendships/received/", FriendshipsReceivedView.as_view()),
    path("friendships/requested/", FriendshipsRequestedView.as_view())
]
