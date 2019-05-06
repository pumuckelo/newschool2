from rest_framework import routers
from .api import PostViewSet

router = routers.DefaultRouter()
router.register('api/classroom', PostViewSet, 'Posts')

urlpatterns = router.urls
