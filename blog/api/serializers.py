from rest_framework.serializers import ModelSerializer
from ..models import Post



class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'date_posted',
        ]

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'date_posted',
        ]


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            'content',
            'date_posted',
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
