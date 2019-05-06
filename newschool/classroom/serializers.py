from rest_framework import serializers
from .models import Post

#Post Serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
