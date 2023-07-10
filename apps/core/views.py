from __future__ import annotations

from django.contrib.auth import login
from django.contrib.auth import logout
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.core.serializer import CreateUserSerializer
from apps.core.serializer import LoginSerializer
from apps.core.serializer import ProfileSerializer
from apps.core.serializer import UpdatePasswordSerializer


class SingUpView(CreateAPIView):
    """Регистрация нового пользователя"""
    serializer_class = CreateUserSerializer


class LoginView(CreateAPIView):
    """Вход по имени и паролю"""
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request=request, user=serializer.save())
        return Response(serializer.data)


class ProfileView(RetrieveUpdateDestroyAPIView):
    """Редактирование данных пользователя"""
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def perform_destroy(self, instance):
        """Logout текущего пользователя"""
        logout(self.request)


class UpdatePassword(UpdateAPIView):
    """Обновление пароля"""
    serializer_class = UpdatePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
