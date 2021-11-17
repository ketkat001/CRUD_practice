from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Article
from .permissions import IsArticleAuthorOrReadOnly
from .serializers import ArticleSerializer
from backend.pagination import CustomPagination


class ArticleAPI(generics.GenericAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    pagination_class = CustomPagination

    
    def get(self, request):
        queryset = Article.objects.all()
        page = self.paginate_queryset(queryset)
        serializer = ArticleSerializer(page, many=True)
        result = self.get_paginated_response(serializer.data)
        return Response(result.data)


    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ArticleDetailAPI(generics.GenericAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsArticleAuthorOrReadOnly]
    def get(self, request, pk):
        article = generics.get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


    def put(self, request, pk):
        article = generics.get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            if article.user != request.user:
                return Response(serializer.errors)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def delete(self, request, pk):
        article = generics.get_object_or_404(Article, pk=pk)
        article.delete()
        return Response('Successful delete')