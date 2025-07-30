from rest_framework import routers

from django.urls import include, path

from events.router import EventsViewSet

router = routers.DefaultRouter()
router.register('', EventsViewSet)

app_name = 'events'
urlpatterns = [
    path('', include(router.urls)),
]
