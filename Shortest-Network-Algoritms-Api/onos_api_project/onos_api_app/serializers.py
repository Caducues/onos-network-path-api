from rest_framework import serializers

class PathRequestSerializer(serializers.Serializer):
    src = serializers.CharField()
    dst = serializers.CharField()
