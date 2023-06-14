from rest_framework.views import APIView, Response, Request, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from friendships.models import Friendship
from friendships.permissions import FriendShipsPermission
from users.models import User
from .serializers import FriendshipSerializer


class FriendshipsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [FriendShipsPermission]

    def get(self, req: Request) -> Response:
        user_id = req.user
        friends = Friendship.objects.filter(status="accepted")
        your_friends = [
            n
            for n in friends
            if n.user_requesting == user_id or n.user_receiving == user_id
        ]
        serializer = FriendshipSerializer(your_friends, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class FriendshipsReceivedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [FriendShipsPermission]

    def get(self, req: Request) -> Response:
        user_id = req.user
        friends = Friendship.objects.filter(status="requested")
        your_friends = [n for n in friends if n.user_receiving == user_id]
        serializer = FriendshipSerializer(your_friends, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class FriendshipsRequestedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [FriendShipsPermission]

    def get(self, req: Request) -> Response:
        user_id = req.user
        friends = Friendship.objects.filter(status="requested")
        your_friends = [n for n in friends if n.user_requesting == user_id]
        serializer = FriendshipSerializer(your_friends, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class FriendshipsDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [FriendShipsPermission]

    def post(self, req: Request, pk: int):
        user_requesting = req.user
        user_receiving = get_object_or_404(User, id=pk)

        if user_requesting == user_receiving:
            return Response(
                data={"detail": "You can't send invite to yourself"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        verify_user_requesting = Friendship.objects.filter(
            user_requesting=user_requesting, user_receiving=user_receiving
        ).first()

        verify_user_receiving = Friendship.objects.filter(
            user_requesting=user_receiving, user_receiving=user_requesting
        ).first()

        if verify_user_requesting:
            if verify_user_requesting.status == "accepted":
                return Response(
                    data={"detail": f"You are already friends"},
                    status=status.HTTP_409_CONFLICT,
                )

            else:
                return Response(
                    data={
                        "detail": f"You already sent a friend request, your request is pending"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if verify_user_receiving:
            if verify_user_receiving.status == "accepted":
                return Response(
                    data={"detail": f"You are already friends"},
                    status=status.HTTP_409_CONFLICT,
                )

            else:
                return Response(
                    data={
                        "detail": f"This user has already sent you a friend request, the request is pending!"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        invite = Friendship.objects.create(
            user_requesting_id=user_requesting.id, user_receiving_id=user_receiving.id
        )
        serializer = FriendshipSerializer(invite)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, req: Request, pk: int) -> Response:
        user_id = req.user
        invite = get_object_or_404(
            Friendship, user_receiving=user_id, user_requesting=pk, status="requested"
        )
        serializer = FriendshipSerializer(
            invite, data={"status": "accepted"}, partial=True
        )
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def delete(self, req: Request, pk: int) -> Response:
        user_id = req.user
        friend = get_object_or_404(User, id=pk)
        verifyRequested = Friendship.objects.filter(
            user_requesting=user_id, user_receiving=friend
        )
        verifyReceived = Friendship.objects.filter(
            user_requesting=friend, user_receiving=user_id
        )

        if len(verifyRequested) == 0 and len(verifyReceived) == 0:
            return Response(
                data={"detail": f"You are not friends!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if verifyRequested:
            verifyRequested.delete()

        if verifyReceived:
            verifyReceived.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
