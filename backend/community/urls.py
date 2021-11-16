from django.urls import path
from .views import ArticleAPI

urlpatterns = [
    path('', ArticleAPI.as_view()),
]