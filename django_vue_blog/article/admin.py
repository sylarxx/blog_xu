from django.contrib import admin
from .models import Article
# Register your models here.

# 注册Article到admin中
admin.site.register(Article)
