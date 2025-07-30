from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'description',
            'date',
            'media_url',
            'album_url',
            'on_map_url',
            'docs_url',
            'registration_url',
            'background_img',
        )
        extra_kwargs = {
            'description': {'required': False},
            'date': {'required': False},
            'media_url': {'required': False},
            'album_url': {'required': False},
            'on_map_url': {'required': False},
            'docs_url': {'required': False},
            'registration_url': {'required': False},
            'background_img': {'required': False},
        }
        read_only_fields = ('id', )
