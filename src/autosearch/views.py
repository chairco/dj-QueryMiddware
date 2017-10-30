from django.http import HttpResponse, Http404, JsonResponse
from django.db.utils import DatabaseError

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework import mixins

from autosearch import query, serializers

from itertools import chain

from datetime import datetime


class EdcGlassHistoryList(APIView):
    """List all glass history.
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
        serializer = EdcGlasshisSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EdcSummaryList(APIView):
    """List all glass summary.
    Example: http://localhost:8000/autosearch/edcs/?glassid=TL6AJ0HAV&stepid=1200&starttime=20161020012712
    """

    def get(self, requests, format=None):
        """glass_id is list type, should be type check and transfer.
        """
        glass_id = requests.GET.get('glassid', None)
        step_id = requests.GET.get('stepid', None)
        start_time = requests.GET.get('starttime', None)
        starttime = datetime.strptime(str(20161020012712), "%Y%m%d%H%M%S")
        queryset = query.get_edc_data(glass_id, step_id, start_time)
        serializer = serializers.EdcSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, requests, format=None):
        body_unicode = requests.body.decode('utf-8')
        body = json.loads(body_unicode)
        glass_id = body.get('glassid', None), 
        step_id = body.get('stepid', None)
        start_time = body.get('starttime', None)
        queryset = query.get_edc_data(glass_id, step_id, start_time)
        serializer = EdcGlasshisSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TegGlassHistoryList(APIView):
    pass


class TegSummaryList(APIView):
    pass
