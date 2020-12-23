from django.urls import path
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView,
    PostCreateAPIView,
)


app_name = 'posts-api'
urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:pk>/update/', PostUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='delete'),
]


# #### TODO ListA
# 先把corey的功能加上去補齊
# 然後可能要把try django or advancing blog看一看
# 需要把comment的部分弄上去
# #####
