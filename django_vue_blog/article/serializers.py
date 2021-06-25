from django.db.models import fields
from rest_framework import serializers
from .models import Article
from user_info.serializers import UserDescSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'created',
            'author'
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # 使用所有字段
        fields = '__all__'
