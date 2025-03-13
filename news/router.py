from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from news.models import NewsRecord
from news.serializers import NewsRecordSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = NewsRecord.objects.all()
    serializer_class = NewsRecordSerializer
    pagination_class = LimitOffsetPagination
