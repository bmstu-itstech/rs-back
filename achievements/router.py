from rest_framework import viewsets

from achievements.models import Achievement
from achievements.serializers import AchievementSerializer

from utils.pagination import CustomPagination, CustomListView


class AchievementsViewSet(CustomListView, viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = CustomPagination
