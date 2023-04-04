from __future__ import annotations

from django.urls import path
from rest_framework import routers

from core.views import LoginView
from core.views import ProfileView
from core.views import SingUpView
from core.views import UpdatePassword

urlpatterns = [
    path('signup', SingUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('update_password', UpdatePassword.as_view(), name='update_password'),
]
