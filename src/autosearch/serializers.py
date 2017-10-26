from rest_framework import serializers


class GlasshisSerializer(serializers.Serializer):
    GLASS_ID = serializers.CharField()
    STEP_ID = serializers.CharField()
    GLASS_START_TIME = serializers.DateTimeField() 