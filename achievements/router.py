from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from achievements.models import Achievement
from achievements.serializers import AchievementSerializer


class AchievementsViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = LimitOffsetPagination
