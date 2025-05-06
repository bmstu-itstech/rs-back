from rest_framework import serializers

from hardathons.models import Hardathon


class HardathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hardathon
        fields = (
            'id',
            'date',
            'start_date',
            'end_date',
            'result',
            'place',
            'media',
            'projects',
            'images',
            'documents',
            'partners',
        )
        extra_kwargs = {
            'start_date': { 'required': False },
            'end_date': { 'required': False },
            'result': { 'required': False },
            'place': { 'required': False },
            'media': { 'required': False },
            'projects': { 'required': False },
            'images': { 'required': False },
            'documents': { 'required': False },
            'partners': { 'required': False },
        }
