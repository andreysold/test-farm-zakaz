from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from apps.participant.serializers.serializers import ParticipantSerializer, ParticipantRetrieveSerializer, \
    ParticipantStartSerializer
from rest_framework import status
from apps.participant.services.participant_service import ParticipantService


class ParticipantCreateApi(GenericAPIView):
    serializer_class = ParticipantSerializer

    def get_response(self, participant):
        response_data = {
            "first_name": getattr(participant, "first_name"),
            "last_name": getattr(participant, "last_name"),
            "age": getattr(participant, "age"),
            "city": getattr(participant, "city")
        }
        return Response(data=response_data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = ParticipantService()

        participant = service.create_participant(**serializer.validated_data)
        response = self.get_response(participant)
        return response


class ParticipantListApi(GenericAPIView):
    serializer_class = ParticipantRetrieveSerializer

    def get(self, request):
        service = ParticipantService()

        list_participants = service.list()
        serializer = self.get_serializer(list_participants, many=True)
        return Response(data=serializer.data)


class ParticipantStartApi(GenericAPIView):
    serializer_class = ParticipantStartSerializer

    def get(self, request):
        service = ParticipantService()

        value = service.start_lottery()
        serializer = self.get_serializer(value)
        return Response(data=serializer.data)
