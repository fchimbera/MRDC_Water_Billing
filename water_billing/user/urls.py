from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserProfileAPIView
from django.conf import settings 
from . import views


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('profile/', UserProfileAPIView.as_view(), name='user-profile'),
]
