from rest_framework import viewsets

import common
from news.models import NewsRecord
from news.serializers import NewsRecordSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = NewsRecord.objects.all()
    serializer_class = NewsRecordSerializer
    pagination_class = common.PaginationMeta(page_size=16)
