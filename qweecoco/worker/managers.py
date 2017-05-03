# -*- coding: utf-8 -*-
from django.contrib.auth.base_user import BaseUserManager


# Модель-менеджер работника (переопределённая стандартная модель-менеджер пользователя)
class WorkerManager(BaseUserManager):

# Переопределённый стандартный метод создание пользователя
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Field Email is required')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

# Переопределённый стандартный метод создание супер-пользователя
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
