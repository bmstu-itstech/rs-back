from rest_framework import viewsets, response
from rest_framework.pagination import LimitOffsetPagination

from events.models import Event
from events.serializers import EventSerializer


class CustomPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        return response.Response({
            "count": self.count,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data
        })


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        if 'limit' in request.query_params:
            self.pagination_class = CustomPagination
        else:
            self.pagination_class = None

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return response.Response({
            "count": queryset.count(),
            "next": None,
            "previous": None,
            "results": serializer.data
        })
