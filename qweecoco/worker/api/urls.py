# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from worker.api.viewsets import WorkerViewSet


# Создание и регистрация маршрутов Urls
router = DefaultRouter()
router.register(r'worker', WorkerViewSet)

# Подключение маршрутов Urls
urlpatterns = [
    url(r'^', include(router.urls)),
]
