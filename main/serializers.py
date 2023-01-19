from rest_framework import serializers


class CreateDefintionSerializer(serializers.Serializer):
    term = serializers.CharField(required=True)
    definition = serializers.CharField(required=True)
