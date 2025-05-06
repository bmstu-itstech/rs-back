from rest_framework import viewsets

from hardathons.models import Hardathon
from hardathons.serializers import HardathonSerializer

from utils.pagination import CustomPagination, CustomListView


class HardathonsViewSet(CustomListView, viewsets.ModelViewSet):
    queryset = Hardathon.objects.all()
    serializer_class = HardathonSerializer
    pagination_class = CustomPagination
