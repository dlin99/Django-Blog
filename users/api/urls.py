from django.urls import path

from .views import (
	UserCreateAPIView
)


app_name = 'users-api'
urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),

]