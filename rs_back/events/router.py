from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rs_back.events.models import ClassicEvent, Questionnaire
from rs_back.events.serializers import (ClassicEventByIdSerializer,
                                        ClassicEventsSerializer,
                                        QuestionnaireByIdSerializer,
                                        QuestionnairesSerializer)


class ClassicEventViewSet(APIView):
    """
    API view для классических мероприятий
    Возвращает json всех мероприятий или детальную информацию одного мероприятия,
    если дополнительно передать pk объекта
    """

    def get(self, request, pk=None):
        data = {}
        if pk:
            classic_event = get_object_or_404(ClassicEvent, pk=pk)
            serializer = ClassicEventByIdSerializer(classic_event)
            data = serializer.data
        else:
            classic_events = ClassicEvent.get_all_objects_by_id()
            serializer = ClassicEventsSerializer(instance=classic_events, many=True)
            data = {
                'count': len(classic_events),
                'events': serializer.data
            }
        return Response(data)


class QuestionnaireViewSet(APIView):
    """
    API view для анкеты
    Возвращает json всех анкет или детальную информацию одной анкеты,
    если дополнительно передать pk объекта
    """

    def get(self, request, pk=None):
        data = {}
        if pk:
            questionnaire = get_object_or_404(Questionnaire, pk=pk)
            serializer = QuestionnaireByIdSerializer(questionnaire)
            data = serializer.data
        else:
            questionnaires = Questionnaire.get_all_objects_by_id()
            serializer = QuestionnairesSerializer(instance=questionnaires, many=True)
            data = {
                'count': len(questionnaires),
                'questionnaires': serializer.data
            }
        return Response(data)
