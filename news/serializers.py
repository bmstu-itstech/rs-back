from rest_framework import serializers

from news.models import NewsRecord


class NewsRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsRecord
        fields = (
            'id',
            'title',
            'content',
            'href',
            'image',
        )
        extra_kwargs = {
            'title': {'required': False},
            'content': {'required': False},
            'href': {'required': False},
            'image': {'required': False},
        }
        read_only_fields = ('id', )
