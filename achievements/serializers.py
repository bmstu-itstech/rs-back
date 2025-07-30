from rest_framework import serializers

from achievements.models import Achievement


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            'id',
            'title',
            'description',
            'album_url',
            'media_url',
            'image',
        )
        extra_kwargs = {
            'description': {'required': False},
            'album_url': {'required': False},
            'media_url': {'required': False},
            'image': {'required': False},
        }
        read_only_fields = ('id', )
