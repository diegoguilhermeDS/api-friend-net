from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from django.http import Http404
from followers.permissions import FollowersPermission

from users.models import User
from .models import Follower
from .serializers import FollowerSerializer


class FollowersDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [FollowersPermission]

    def post(self, req: Request, pk: int) -> Response:
        user_following = req.user
        user_followed = get_object_or_404(User, pk=pk)

        if user_following == user_followed:
            return Response(
                data={"detail": "You can't follow yourself"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        follow = Follower.objects.filter(
            user_following=user_following, user_followed=user_followed
        ).first()

        if follow:
            return Response(
                data={"detail": f"You already follow the user {pk}"},
                status=status.HTTP_409_CONFLICT,
            )

        follow = Follower.objects.create(
            user_following=user_following, user_followed=user_followed
        )

        serializer = FollowerSerializer(follow)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        user_following = request.user
        user_followed = get_object_or_404(User, pk=pk)
        try:
            follow_found = get_object_or_404(
                klass=Follower,
                user_following=user_following,
                user_followed=pk
            )
        except Http404:
            return Response(
                {"message": f"You don't follow user {pk}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        follow_found.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FollowersIFollowView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [FollowersPermission]

    def get(self, req: Request) -> Response:
        user = req.user

        i_follow = Follower.objects.filter(
            user_following=user
        )

        if not i_follow:
            return Response(
                data={"detail": "You don't follow anyone"},
                status=status.HTTP_200_OK
            )

        serializer = FollowerSerializer(i_follow, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class FollowersMyFollowersView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [FollowersPermission]

    def get(self, req: Request) -> Response:
        user = req.user

        i_follow = Follower.objects.filter(
            user_followed=user
        )

        if not i_follow:
            return Response(
                data={"detail": "Nobody follows you."},
                status=status.HTTP_200_OK
            )

        serializer = FollowerSerializer(i_follow, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
