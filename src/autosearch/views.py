from django.http import HttpResponse, Http404, JsonResponse
from django.db.utils import DatabaseError

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework import mixins

from autosearch import query, serializers

from itertools import chain


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
    Example: http://localhost:8000/autosearch/edcs/?glassid=TL6AS0KAF
    """
    serializer_class = serializers.EdcSerializer


    def get(self, requests, format=None):
        """glass_id is list type, should be type check and transfer.
        """
        glass_id = requests.GET.get('glassid', None)
        if glass_id != None:
            glass_id = [g.strip() for g in glass_id.split(',')]
        
        datas = query.query_edch_concurrency(query.get_edc_glass_history, glass_id)
        values = list(chain.from_iterable(datas.values()))
        queryset = query.query_edcs_concurrency(query.get_edc_data, values)
        #serializers = serializers.EdcSerializer(queryset, many=True)
        #return Response(serializer.data)
        json = JSONRenderer().render(queryset)
        return Response(json, status=status.HTTP_200_OK)

    def post(self, requests, format=None):
        body_unicode = requests.body.decode('utf-8')
        body = json.loads(body_unicode)
        glass_id = body.get('glassid', None)
        queryset = query.get_edc_glass_history(glass_id)
        serializer = EdcGlasshisSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TegGlassHistoryList(APIView):
    pass


class TegSummaryList(APIView):
    pass
