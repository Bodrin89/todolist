from __future__ import annotations

from django.urls import path

from goals import views

urlpatterns = [
    path('goal_category/create', views.GoalCategoryCreateView.as_view(), name='create_category'),
    path('goal_category/list', views.GoalCategoryListView.as_view(), name='category_list'),
    path('goal_category/<int:pk>', views.GoalCategoryView.as_view(), name='goal_category'),
]
