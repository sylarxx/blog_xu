from .serializers import ArticleSerializer
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import permissions
from rest_framework import views
from .models import Article
#from .serializers import ArticleListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from django.http import Http404
#from .serializers import ArticleDetailSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminUserOrReadOnly


'''
# Create your views here.
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]
'''

# @api_view装饰器允许视图接收GET,POST请求
'''
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    # 文章详情视图
    def get_object(self, pk):
        # 获取单个文章对象
        try:
            # pk即主键primary key， 默认状态下是id
            return Article.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article)
        # 返回JSON数据
        return Response(serializer.data)

    # 修改文章
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article, data=request.data)
        # 验证提交的数据是否合法
        # 不合法则返回400
        if serializer.is_valid():
            # 序列化器将持有的数据反序列化后
            # 保存到数据库中
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        # 删除成功后返回204
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
