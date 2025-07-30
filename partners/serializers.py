from rest_framework import serializers

from partners.models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = (
            'id',
            'name',
            'url',
            'logo',
        )
        extra_kwargs = {
            'name': {'required': False},
            'url': {'required': False},
            'logo': {'required': False},
        }
        read_only_fields = ('id', )
