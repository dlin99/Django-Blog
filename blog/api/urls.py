from django.urls import path
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView,
)


app_name = 'posts-api'
urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update/', PostUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='delete'),
    # path('about/', views.about, name='blog-about'),
]

# <app>/<model>_<viewtype>.html
#
# urlpatterns = [
#     path('', views.home, name='blog-home'),
#     path('about/', views.about, name='blog-about'),
# ]
