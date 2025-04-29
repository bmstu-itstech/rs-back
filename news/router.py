from rest_framework import viewsets

from news.models import NewsRecord
from news.serializers import NewsRecordSerializer

from utils.pagination import CustomPagination, CustomListView


class NewsViewSet(CustomListView, viewsets.ModelViewSet):
    queryset = NewsRecord.objects.all()
    serializer_class = NewsRecordSerializer
    pagination_class = CustomPagination
