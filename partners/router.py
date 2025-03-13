from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from partners.models import Partner
from partners.serializers import PartnerSerializer


class PartnersViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    pagination_class = LimitOffsetPagination
