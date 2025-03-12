from django.urls import include, path
from rest_framework import routers

from partners.router import PartnersViewSet

router = routers.DefaultRouter()
router.register('', PartnersViewSet)

app_name = 'partners'
urlpatterns = [
    path('', include(router.urls)),
]
