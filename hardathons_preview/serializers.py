from rest_framework import serializers

from hardathons_preview.models import HardathonPreview


class HardathonPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardathonPreview
        fields = (
            'id',
            'href',
            'title',
            'photo',
        )
        extra_kwargs = {
            'photo': { 'required': False },
        }
