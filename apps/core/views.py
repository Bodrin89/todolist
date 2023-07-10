from __future__ import annotations

from django.contrib.auth import login, logout
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.core.models import User
from apps.core.serializer import CreateUserSerializer, LoginSerializer, ProfileSerializer, UpdatePasswordSerializer


class SingUpView(CreateAPIView):
    serializer_class = CreateUserSerializer


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request=request, user=serializer.save())
        return Response(serializer.data)


class ProfileView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def perform_destroy(self, instance):
        logout(self.request)


class UpdatePassword(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdatePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
