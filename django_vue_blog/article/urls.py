from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('/<int:pk>', views.ArticleDetail.as_view(), name='detail'),
]
