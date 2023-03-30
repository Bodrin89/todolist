from __future__ import annotations

from django.urls import path

from core.views import SingUpView

urlpatterns = [
    path('signup', SingUpView.as_view(), name='signup')
]
