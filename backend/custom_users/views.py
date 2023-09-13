# Create your views here.

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from backend.custom_users.models import CustomUser
from backend.custom_users.serializers import (
    CustomUserSerializer,
)


class UserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Save the user instance
            self.perform_create(serializer)
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserProfileView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_object(self):
        # Retrieve the user associated with the request
        return self.request.user
