from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    )

from blog.models import Post

from comments.models import Comment 
from comments.api.serializers import CommentSerializer


post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='pk'
    )


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    author = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'author',
            'title',
            'content',
            'date_posted',
        ]

    def get_author(self, obj):
        return str(obj.author.username)

class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    author = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'author',
            'title',
            'content',
            'html',
            'date_posted',
            'comments',
        ]

    def get_author(self, obj):
        return str(obj.author.username)

    def get_html(self, obj):
        return obj.get_markdown()

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            'content',
            'date_posted',
            # 'author',
        ]


"""
### similar to form in django

data = {
    "title": "hahaha",
    "content": "New Content",
    "date_posted": "2020-02-22"
}

new_item = PostSerializer(data=data)

if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)


### update an new_item

obj = Post.objects.get(id=2)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
"""
