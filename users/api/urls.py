from django.urls import path

from .views import (
	UserCreateAPIView,
	UserLoginAPIView,
)


app_name = 'users-api'
urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
]
