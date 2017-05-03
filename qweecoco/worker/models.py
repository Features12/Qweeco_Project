# -*- coding: utf-8 -*-
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.mail import send_mail
from worker.managers import WorkerManager
from worker.settings import ROLES_EMPLOYEES, ROLE_DEVELOPER


# Модель работника (переопределённая стандартная модель пользователя)
class Worker(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    date_of_birth = models.DateField(verbose_name='date of birth', default='1990-12-12')
    is_active = models.BooleanField(verbose_name='active', default=True)
    age = models.PositiveIntegerField(verbose_name='age', default=21)
    start_date_of_work = models.DateField(verbose_name='start date of work', auto_now_add=True)
    role = models.CharField(verbose_name='role employee', choices=ROLES_EMPLOYEES, max_length=100, default=ROLE_DEVELOPER)
    middle_name = models.CharField(verbose_name='middle name', max_length=50, blank=True)
    is_admin = models.BooleanField(verbose_name='staff status', default=False)

# Переопределён стандартный метод получения полного имени, унаследованного класса AbstractBaseUser
    def get_full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)

# Переопределён стандартный метод получения доступа к интерфейсу администратора
    def is_staff(self):
        return self.is_admin

# Переопределён стандартный метод получения короткого имени, унаследованного класса AbstractBaseUser
    def get_short_name(self):
        return self.first_name

# Метод отправки электронной почты пользователю
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

# Переопределён стандартный метод по проверке прав, унаследованного класса PermissionsMixin
    def has_perm(self, perm, obj=None):
        return True

# Переопределён стандартный метод по проверке прав, унаследованного класса PermissionsMixin
    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

# Переопределено имя поля модели, которое используется для уникального идентификатора
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

# QuerySet метод для объектов Worker
    objects = WorkerManager()

# Читабельное название модели в единственном и множественном числе
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
