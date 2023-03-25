from rest_framework import serializers


class ParticipantSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, max_length=256)
    last_name = serializers.CharField(required=True, max_length=256)
    age = serializers.IntegerField(required=False)
    city = serializers.CharField(required=False, max_length=256)


class ParticipantRetrieveSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=256)
    last_name = serializers.CharField(max_length=256)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=256)

class ParticipantStartSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, max_length=256)
    last_name = serializers.CharField(required=True, max_length=256)
    age = serializers.IntegerField(required=False)
    city = serializers.CharField(required=False, max_length=256)
    win = serializers.IntegerField(read_only=True)