from rest_framework import viewsets

from hardathons_preview.models import HardathonPreview
from hardathons_preview.serializers import HardathonPreviewSerializer

from utils.pagination import CustomPagination, CustomListView


class HardathonsPreviewViewSet(CustomListView, viewsets.ModelViewSet):
    queryset = HardathonPreview.objects.all()
    serializer_class = HardathonPreviewSerializer
    pagination_class = CustomPagination
