from django.urls import include, path
from rest_framework import routers

from achievements.router import AchievementsViewSet


router = routers.DefaultRouter()
router.register('', AchievementsViewSet)

app_name = 'achievements'
urlpatterns = [
    path('', include(router.urls)),
]
