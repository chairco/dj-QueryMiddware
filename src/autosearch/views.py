# -*- coding:utf-8 -*-
from django.http import HttpResponse, Http404, JsonResponse
from django.db.utils import DatabaseError

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework import mixins

from autosearch import query, serializers

from datetime import datetime

from dateutil.parser import parse


class EdcGlassHistoryList(APIView):
    """List all glass edc history.
    Example: http://localhost:8000/autosearch/edch/?glassid=TL6AS0KAF
    """

    def get(self, requests, format=None):
        """glass_id is list type, should be type check and transfer.
        """
        glass_id = requests.GET.get('glassid', None)
        queryset = query.get_edc_glass_history(glass_id)
        serializer = serializers.EdcGlasshisSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, requests, format=None):
        body_unicode = requests.body.decode('utf-8')
        body = json.loads(body_unicode)
        glass_id = body.get('glassid', None)
        queryset = query.get_edc_glass_history(glass_id)
        serializer = serializers.EdcGlasshisSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EdcSummaryList(APIView):
    """List all glass edc summary.
    Example: 
        http://localhost:8000/autosearch/edcs/?glassid=TL6AJ0HAV&stepid=1200&starttime=20161020012712
    """

    def get(self, requests, format=None):
        """glass_id is list type, should be type check and transfer.
        """
        glass_id = requests.GET.get('glassid', None)
        step_id = requests.GET.get('stepid', None)
        start_time = requests.GET.get('starttime', None)
        # Convert timestamps with parser method.
        # 注意傳遞過程 2016-11-10T00:54:22+08:00 時區 + 號會被拿掉要在後端先處理過。
        # https://stackoverflow.com/questions/12281975/convert-timestamps-with-offset-to-datetime-obj-using-strptime
        # http://labix.org/python-dateutil#head-a23e8ae0a661d77b89dfb3476f85b26f0b30349c
        start_time = parse(start_time)
        queryset = query.get_edc_data(glass_id, step_id, start_time)
        serializer = serializers.EdcSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, requests, format=None):
        body_unicode = requests.body.decode('utf-8')
        body = json.loads(body_unicode)
        glass_id = body.get('glassid', None), 
        step_id = body.get('stepid', None)
        start_time = body.get('starttime', None)
        start_time = parse(start_time)
        queryset = query.get_edc_data(glass_id, step_id, start_time)
        serializer = serializers.EdcGlasshisSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TegGlassHistoryList(APIView):
    """List all glass teg history.
    Example:
        Example: http://localhost:8000/autosearch/tegh/?glassid=TL6AS0KAF
    """
    def get(self, requests, format=None):
        glass_id = requests.GET.get('glassid', None)
        queryset = query.get_teg_glass_history(glass_id)
        serializer = serializers.TegGlasshisSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, requests, format=None):
        pass


class TegSummaryList(APIView):
    """List all glass teg summary.
    Example:
        http://localhost:8000/autosearch/tegs/?glassid=TL6AS0KAF&stepid=2230&starttime=20161027173851
    """
    def get(self, requests, format=None):
        glass_id = requests.GET.get('glassid', None)
        step_id = requests.GET.get('stepid', None)
        start_time = requests.GET.get('starttime', None)
        start_time = parse(start_time)
        queryset = query.get_teg_data(glass_id, step_id, start_time)
        serializer = serializers.TegSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, requests, format=None):
        pass
