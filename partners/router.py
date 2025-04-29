from rest_framework import viewsets

from partners.models import Partner
from partners.serializers import PartnerSerializer

from utils.pagination import CustomPagination, CustomListView


class PartnersViewSet(CustomListView, viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    pagination_class = CustomPagination
