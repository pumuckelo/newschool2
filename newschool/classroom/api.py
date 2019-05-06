from .models import Post
from rest_framework import viewsets, permissions
from .serializers import PostSerializer

#Post Viewset, allows to create a Full Crud API without bla bla keine Ahnung
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer