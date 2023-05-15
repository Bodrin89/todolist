from __future__ import annotations

from typing import Any

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import SAFE_METHODS
from rest_framework.request import Request

from apps.goals.models import Board
from apps.goals.models import BoardParticipant
from apps.goals.models import GoalCategory


class BoardPermission(IsAuthenticated):

    def has_object_permission(self, request: Request, view, obj: Board) -> bool:
        _filters: dict[str: Any] = {'user_id': request.user.id, 'board_id': obj.id}
        if request.method not in SAFE_METHODS:
            _filters['role'] = BoardParticipant.Role.owner
        return BoardParticipant.objects.filter(**_filters).exists()


class GoalCategoryPermission(IsAuthenticated):

    def has_object_permission(self, request: Request, view, goal_category: GoalCategory) -> bool:
        _filters: dict[str: Any] = {'user_id': request.user.id, 'board_id': goal_category.board_id}
        if request.method not in SAFE_METHODS:
            _filters['role'] = BoardParticipant.Role.owner
        return BoardParticipant.objects.filter(**_filters).exists()
