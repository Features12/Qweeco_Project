# -*- coding: utf-8 -*-
from rest_framework import serializers
from worker.models import Worker


# Создание Serializer для модели Worker
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker # Принимает на вход модель Worker
        fields = ('id', 'email', 'first_name', 'last_name', 'middle_name', 'role', 'is_active', 'date_of_birth') # Поля модели Worker, которые будут сериализованы
        