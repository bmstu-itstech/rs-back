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
