from enum import auto
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# BLOG Article Form
# models.Model 继承了操作数据库需要的所有办法


class Article(models.Model):
    # 作者
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='article'
    )

    # 标题
    title = models.CharField(max_length=100)

    # 正文
    body = models.TextField()

    # 创建时间
    # 参数 default=timezone.now 指在创建数据时将默认写入当前时间
    created = models.DateTimeField(default=timezone.now)

    # 更新时间
    # 参数 auto_now=True 指每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    # 在类中的str方法是在打印类的实例对象时，调用该方法，一般返回一个字符串
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
