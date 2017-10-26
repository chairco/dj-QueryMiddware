from django.http import HttpResponse, Http404, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from autosearch import query


@api_view(['GET', 'POST'])
def edc_glass_history(requests):
    """API endpoint that allo connect Oracle db.
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
    return Response(json)
