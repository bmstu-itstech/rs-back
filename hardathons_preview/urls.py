from django.urls import include, path
from rest_framework import routers

from hardathons_preview.router import HardathonsPreviewViewSet

router = routers.DefaultRouter()
router.register('', HardathonsPreviewViewSet)

app_name = 'hardathons_preview'
urlpatterns = [
    path('', include(router.urls)),
]
