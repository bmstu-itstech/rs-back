from rest_framework.response import Response
from rest_framework.views import APIView

from rs_back.news.models import News
from rs_back.news.serializers import NewsSerializer


class NewsViewSet(APIView):
    """
    API view для новостей
    Возвращает json всех новостей в порядке их создания
    """

    def get(self, request, format=None):
        news = News.get_all_objects_by_id()
        serializer = NewsSerializer(instance=news, many=True)
        data = {
            'count': len(news),
            'news': serializer.data
        }
        return Response(data)
