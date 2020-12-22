from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView
)

from .. models import Post
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer
)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'slug'
    # lookup_url_kwarg = 'abc' # /<abc>/

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'slug'
    # lookup_url_kwarg = 'abc' # /<abc>/

class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'slug'
    # lookup_url_kwarg = 'abc' # /<abc>/

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
