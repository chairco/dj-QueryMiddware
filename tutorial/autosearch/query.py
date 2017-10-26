from django.db import connections


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_edc_glass_history(glass_id):
    """query edc db data
    """
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
        queryset = dictfetchall(cursor)
    return queryset