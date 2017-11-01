from rest_framework import serializers


class EdcGlasshisSerializer(serializers.Serializer):
    GLASS_ID = serializers.CharField()
    STEP_ID = serializers.CharField()
    GLASS_START_TIME = serializers.DateTimeField()
    SUB_EQUIP_ID = serializers.CharField()


class EdcSerializer(serializers.Serializer):
    GLASS_ID = serializers.CharField()
    STEP_ID = serializers.CharField()
    GLASS_START_TIME = serializers.DateTimeField()
    SUB_EQUIP_ID = serializers.CharField()
    PARAM_NAME = serializers.CharField()
    PARAM_VALUE = serializers.FloatField()


class TegGlasshisSerializer(serializers.Serializer):
    GLASS_ID = serializers.CharField()
    STEP_ID = serializers.CharField()
    GLASS_START_TIME = serializers.DateTimeField()


class TegSerializer(serializers.Serializer):
    GLASS_ID = serializers.CharField()
    STEP_ID = serializers.CharField()
    GLASS_START_TIME = serializers.DateTimeField()
    PARAM_NAME = serializers.CharField()
    PARAM_VALUE = serializers.FloatField()
    TTL_COUNT = serializers.IntegerField()
    AVG_VALUE = serializers.FloatField()
    STD_VALUE = serializers.FloatField()
    MAX_VALUE = serializers.FloatField()
    MIN_VALUE = serializers.FloatField()
    RANGE_VALUE = serializers.FloatField()
    UNI_VALUE = serializers.FloatField()
    MEDIAN_VALUE = serializers.FloatField()
    Q1_VALUE = serializers.FloatField()
    Q3_VALUE = serializers.FloatField()
