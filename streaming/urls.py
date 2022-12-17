from rest_framework import routers
from .api import AudiovisualViewSet

router = routers.DefaultRouter()

router.register('api/streaming', AudiovisualViewSet, 'auddivisual')

urlpatterns = router.urls
