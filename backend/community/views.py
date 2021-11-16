from rest_framework import generics
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article


class ArticleAPI(generics.GenericAPIView):
    serializer_class = ArticleSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)