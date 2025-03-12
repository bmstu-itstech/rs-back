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
