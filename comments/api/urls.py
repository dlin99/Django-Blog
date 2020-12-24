from django.urls import path

from .views import (
    CommentListAPIView,
    CommentDetailAPIView,

)


app_name = 'comments-api'
urlpatterns = [
    path('', CommentListAPIView.as_view(), name='list'),
    path('<int:pk>/', CommentDetailAPIView.as_view(), name='thread'),

    # path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='delete'),
]
