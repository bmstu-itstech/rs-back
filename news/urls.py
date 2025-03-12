from django.urls import include, path
from rest_framework import routers

from news.router import NewsViewSet


router = routers.DefaultRouter()
router.register('', NewsViewSet)

app_name = 'news'
urlpatterns = [
    path('', include(router.urls)),
]
