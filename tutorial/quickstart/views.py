from django.contrib.auth.models import User, Group
from django.db import connection, connections

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


@api_view(['GET', 'POST'])
def edc_glass_history(requests, glass_id):
    """
    API endpoint that allo connect Oracle db.
    """
    if requests.method == 'GET':
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
            queryset = cursor.fetchall()
            cursor.close()
        except Exception as e:
            raise e

        return Response(rows)