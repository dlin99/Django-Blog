from django.urls import path

from .views import (
    CommentListAPIView,
    CommentDetailAPIView,
    CommentCreateAPIView,
    # CommentEditAPIView,
)


app_name = 'comments-api'
urlpatterns = [
    path('', CommentListAPIView.as_view(), name='list'),
    path('create/', CommentCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', CommentDetailAPIView.as_view(), name='thread'),
    # path('<int:pk>/edit/', CommentEditAPIView.as_view(), name='edit'), # delete will be an option here

    # path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='delete'),
]
