from django.urls import path
from .views import SignupAPI
urlpatterns = [
    path('signup/', SignupAPI.as_view()),
]   