from rest_framework import serializers

from hardathons.models import Hardathon


class HardathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hardathon
        fields = (
            'id',
            'title',
            'href',
            'background_image',
            'date',
            'start_date',
            'end_date',
            'result_date',
            'place',
            'media',
            'projects',
            'images',
            'documents',
            'partners',
        )
        extra_kwargs = {
            'href': { 'required': False },
            'background_image': { 'required': False },
            'date': { 'required': False },
            'start_date': { 'required': False },
            'end_date': { 'required': False },
            'result_date': { 'required': False },
            'place': { 'required': False },
            'media': { 'required': False },
            'projects': { 'required': False },
            'images': { 'required': False },
            'documents': { 'required': False },
            'partners': { 'required': False },
        }
