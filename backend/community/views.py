from rest_framework import generics, serializers
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article


class ArticleAPI(generics.GenericAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ArticleDetailAPI(generics.GenericAPIView):
    serializer_class = ArticleSerializer


    def get(self, request, pk):
        article = generics.get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


    def put(self, request, pk):
        article = generics.get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def delete(self, request, pk):
        article = generics.get_object_or_404(Article, pk=pk)
        article.delete()
        return Response('Successful delete')