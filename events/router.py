from rest_framework import viewsets

from events.models import Event
from events.serializers import EventSerializer

from utils.pagination import CustomPagination, CustomListView


class EventsViewSet(CustomListView, viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = CustomPagination
