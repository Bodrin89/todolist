from __future__ import annotations

from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from core.serializer import CreateUserSerializer


class SingUpView(CreateAPIView):
    serializer_class = CreateUserSerializer
