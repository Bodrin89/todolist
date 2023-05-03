from __future__ import annotations

from django.urls import path

from apps.core.views import LoginView
from apps.core.views import ProfileView
from apps.core.views import SingUpView
from apps.core.views import UpdatePassword

urlpatterns = [
    path('signup', SingUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('update_password', UpdatePassword.as_view(), name='update_password'),
]
