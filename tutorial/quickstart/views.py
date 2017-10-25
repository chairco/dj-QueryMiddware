from django.contrib.auth.models import User, Group
from django.db import connections

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    from collections import namedtuple

    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


@api_view(['GET', 'POST'])
def edc_glass_history(requests, glass_id):
    """
    API endpoint that allo connect Oracle db.
    """
    if requests.method == 'GET':
        '''
        # content management
        with connections['eda'].cursor() as cursor:
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
        return Response(dictfetchall(cursor))
        '''
        # try..finally
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
            cursor.close()
            queryset = dictfetchall(cursor)
            json = JSONRenderer().render(queryset)
            return Response(json)
        except Exception as e:
            cursor.close()
        