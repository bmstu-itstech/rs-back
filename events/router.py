from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from events.models import Event
from events.serializers import EventSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = LimitOffsetPagination
