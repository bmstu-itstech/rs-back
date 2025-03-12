from rest_framework import viewsets

import common
from events.models import Event
from events.serializers import EventSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = common.PaginationMeta(page_size=16)
