from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer
from knox.models import AuthToken


# Create your views here.

class SignupAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response (
            {
                'user' : UserSerializer(
                    user, context = self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        auth_login(request, user)
        return Response(
            {
                'user': UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                 "token": AuthToken.objects.create(user)[1],
            }
        )