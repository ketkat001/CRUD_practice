from django.urls import path, include
from .views import SignupAPI, LoginAPI


urlpatterns = [
    path('signup/', SignupAPI.as_view()),
    path('login/', LoginAPI.as_view()),
]   