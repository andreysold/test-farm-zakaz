from rest_framework import serializers

from apps.participant.serializers.serializers import ParticipantRetrieveSerializer


class WinnersSerializer(serializers.Serializer):
    win = serializers.IntegerField(required=True)
    participant = ParticipantRetrieveSerializer()
