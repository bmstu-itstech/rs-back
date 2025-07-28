from rest_framework import routers

from django.urls import include, path

from achievements.router import AchievementsViewSet


router = routers.DefaultRouter()
router.register('', AchievementsViewSet)

app_name = 'achievements'
urlpatterns = [
    path('', include(router.urls)),
]
