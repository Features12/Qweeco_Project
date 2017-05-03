# -*- coding: utf-8 -*-
from rest_framework import permissions
from worker.settings import ROLES_WITH_ALL_PRIVILEGES



# Создание модели доступа для удовлетворения след. условий:
# 1. Если пользователь соответсвует самому себе
# 2. Если роль пользователя позволяет произвести это действие
class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE', 'PATCH']: # Для DELETE и PATCH запросов будет производиться одна проверка
            return request.user.role in ROLES_WITH_ALL_PRIVILEGES
        return request.user == obj or request.user.role in ROLES_WITH_ALL_PRIVILEGES # Для всех остальных запросов
