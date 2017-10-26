from django.http import HttpResponse, Http404, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import status

from autosearch import query
from autosearch.serializers import GlasshisSerializer


@api_view(['GET', 'POST'])
def edc_glass_history(requests):
    """API endpoint that allo connect Oracle db.
    Example: http://localhost:8000/autosearch/?glassid=TL6AS0KAF
    """
    if requests.method == 'GET':
        glass_id = requests.GET.get('glassid', None)

    elif requests.method == 'POST':
        body_unicode = requests.body.decode('utf-8')
        body = json.loads(body_unicode)
        glass_id = body.get('glassid', None)

    try:
        queryset = query.get_edc_glass_history(glass_id)
    except Exception as e:
        return HttpResponse(e)

    json = JSONRenderer().render(queryset)
    return Response(json, status=status.HTTP_200_OK)


class EdcGlassHistoryList(APIView):
    """List all glass history.
    Example: http://localhost:8000/autosearch/cbv/?glassid=TL6AS0KAF
    """
    def get(self, requests, format=None):
        glass_id = requests.GET.get('glassid', None)
        queryset = query.get_edc_glass_history(glass_id)
        serializer = GlasshisSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, requests, format=None):
        body_unicode = requests.body.decode('utf-8')
        body = json.loads(body_unicode)
        glass_id = body.get('glassid', None)
        queryset = query.get_edc_glass_history(glass_id)
        serializer = GlasshisSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
