from rest_framework import viewsets

import common
from achievements.models import Achievement
from achievements.serializers import AchievementSerializer


class AchievementsViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = common.PaginationMeta(page_size=16)
