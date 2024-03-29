from django.contrib.auth import models
from django.contrib.auth.models import User
from rest_framework import fields, serializers


class UserDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'last_login',
            'date_joined'
        ]
