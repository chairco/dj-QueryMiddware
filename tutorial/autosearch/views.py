from django.shortcuts import render
from django.db import connections

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


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

    if glass_id == None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        cursor = connections['eda'].cursor()
        cursor.execute(
            """
            SELECT "GLASS_ID", "STEP_ID", "GLASS_START_TIME" 
            FROM lcdsys.array_pds_glass_t t
            WHERE 1=1
            AND t.glass_id = :glass_id
            ORDER BY glass_start_time
            """,
            {'glass_id': glass_id}
        )
        queryset = dictfetchall(cursor)
        cursor.close()
    except Exception as e:
        cursor.close()
        return Response(status=status.HTTP_404_NOT_FOUND)

    json = JSONRenderer().render(queryset)
    return Response(json)
