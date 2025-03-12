from rest_framework import viewsets

import common
from partners.models import Partner
from partners.serializers import PartnerSerializer


class PartnersViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    pagination_class = common.PaginationMeta(page_size=16)
