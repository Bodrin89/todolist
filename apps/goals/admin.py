from __future__ import annotations

from django.contrib import admin

from apps.goals.models import Goal
from apps.goals.models import GoalCategory
from apps.goals.models import GoalComment


@admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'updated')
    search_fields = ('title', 'user__username')
    list_filter = ('is_deleted',)
    search_help_text = 'Поиск по названию категории и имени пользователя'


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'updated')
    search_fields = ('title', 'description')
    list_filter = ('status',)
    search_help_text = 'Поиск по названию и описанию цели'


@admin.register(GoalComment)
class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ('goal', 'user', 'created', 'updated')
    search_fields = ('text',)
    list_filter = ('goal',)
    search_help_text = 'Поиск по тексту в комментарии'
