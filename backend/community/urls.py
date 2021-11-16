from django.urls import path
from .views import ArticleAPI, ArticleDetailAPI

urlpatterns = [
    path('', ArticleAPI.as_view()),
    path('<int:pk>/', ArticleDetailAPI.as_view()),
]