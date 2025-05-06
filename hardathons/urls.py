from django.urls import include, path
from rest_framework import routers

from hardathons.router import HardathonsViewSet

router = routers.DefaultRouter()
router.register('', HardathonsViewSet)

app_name = 'hardathons'
urlpatterns = [
    path('', include(router.urls)),
]
