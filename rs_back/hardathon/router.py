from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rs_back.hardathon.models import Hardathon, Project
from rs_back.hardathon.serializers import (DetailProjectSerializer,
                                           HardathonByIdSerializer,
                                           HardathonSerializer,
                                           HardathonPartnersSerializer,
                                           HardathonProjectsSerializer)


class HardathonViewSet(APIView):
    """
    API view для списка хардатонов
    Возвращает json всех хардатонов в порядке их создания или
    детальную информацию одного хардатона, если дополнительно передать pk объекта
    """

    def get(self, request, pk=None):
        data = {}
        if pk:
            hardathon = get_object_or_404(Hardathon, pk=pk)
            serializer = HardathonByIdSerializer(hardathon)
            data = serializer.data
        else:
            hardathons = Hardathon.get_all_objects_by_id()
            serializer = HardathonSerializer(instance=hardathons, many=True)
            data = {
                'count': len(hardathons),
                'hardathons': serializer.data
            }
        return Response(data)


class HardathonProjectsViewSet(APIView):
    """
    API view для проектов хардатона
    Возвращает json всех проектов или
    детальную информацию одного проекта, если дополнительно передать pk объекта
    """

    def get(self, request, pk=None):
        data = {}
        if pk:
            project = get_object_or_404(Project, pk=pk)
            serializer = DetailProjectSerializer(project)
            data = serializer.data
        else:
            projects = Project.get_all_objects_by_id()
            serializer = HardathonProjectsSerializer(instance=projects, many=True)
            data = {
                'count': len(projects),
                'projects': serializer.data
            }
        return Response(data)


class HardathonPartnersViewSet(APIView):
    """
    API view партнёров хардатона
    Возвращает json партнёров хардатона, переданного по pk
    """

    def get(self, request, pk=None):
        hardathon = get_object_or_404(Hardathon, pk=pk)
        partners = hardathon.partners.all()
        serializer = HardathonPartnersSerializer(instance=partners, many=True)
        data = {
            'count': len(partners),
            'partners': serializer.data
        }
        return Response(data)
