# -*- coding: utf-8 -*-
from rest_framework import viewsets, permissions
from worker.api.permissions import IsOwnerOrAdmin
from worker.api.serialaizers import WorkerSerializer
from worker.models import Worker
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend


# Временное избавление от csrf-проверок
class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


# Создание ViewSet для модели Worker
class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()  # Принимает на вход все объекты модели Worker
    serializer_class = WorkerSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('date_of_birth',)
