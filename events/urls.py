from django.urls import include, path
from rest_framework import routers

from events.router import EventsViewSet

router = routers.DefaultRouter()
router.register('', EventsViewSet)

app_name = 'events'
urlpatterns = [
    path('', include(router.urls)),
]
