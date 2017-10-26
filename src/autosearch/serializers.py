from rest_framework import serializers


class GlasshisSerializer(serializers.Serializer):
    GLASS_ID = serializers.CharField(max_length=None, min_length=None, allow_blank=True, required=False)
    STEP_ID = serializers.CharField(max_length=None, min_length=None, allow_blank=True, required=False)
    GLASS_START_TIME = serializers.DateTimeField() 