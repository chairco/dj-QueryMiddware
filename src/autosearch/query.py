# autosearch/qyery.py
from django.db import connections

from concurrent import futures


MAX_WORKER = 200


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_edc_glass_history(glass_id):
    """From array_pds_glass_t table
    type glass_id: str
    rtype: dict(step_id, glass_id, start_time)
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


def get_edc_data(glass_id, step_id, start_time):
    """From array_pds_glass_summary_v
    :type glass_id: str
    :type step_id: str
    :type start_time: Datatime()
    :rtype: dict()
    """
    with connections['eda'].cursor() as cursor:
        cursor.execute(
            """
            SELECT *
            FROM lcdsys.array_pds_glass_summary_v t
            WHERE 1=1 
            AND t.GLASS_ID = :glass_id
            AND t.STEP_ID = :step_id
            AND t.GLASS_START_TIME = :start_time
            """,
            {
                'glass_id': glass_id,
                'step_id': step_id,
                'start_time': start_time
            }
        )
        queryset = dictfetchall(cursor)
    return queryset


def get_teg_glass_history(glass_id):
    """Here is teg history
    rtype
    """
    with connections['eda'].cursor() as cursor:
        cursor.execute(
            """
            SELECT "GLASS_ID", "STEP_ID", "GLASS_START_TIME"
            FROM lcdsys.array_glass_v t
            WHERE 1=1
            AND t.glass_id = :glass_id
            ORDER BY glass_Start_time ASC
            """,
            {'glass_id': glass_id}
        )
        queryset = dictfetchall(cursor)
    return queryset


def get_teg_data(glass_id, step_id, start_time):
    """Here is teg summary data
    rtype
    """
    with connections['eda'].cursor() as cursor:
        cursor.execute(
            """
            SELECT *
            FROM lcdsys.array_glass_summary_v t
            WHERE 1=1
            AND t.GLASS_ID = :glass_id
            AND t.STEP_ID = :step_id
            AND t.GLASS_START_TIME = :start_time
            """,
            {
                'glass_id': glass_id,
                'step_id': step_id,
                'start_time': start_time
            }
        )
        queryset = dictfetchall(cursor)
    return queryset


def get_teg_param_data(glass_id, step_id, start_time):
    """
    """
    pass


def get_teg_result(glass_id, step_id, start_time, param_name):
    """Here is teg raw data with one
    rtype
    """
    pass


def get_teg_result_sub(glass_id, step_id, start_time):
    """
    """
    pass


def get_sid_with_param(glass_id):
    """
    """
    pass


def query_many(query, glass_id):
    """Query oracle db by mutiplethread
    :type query: query object
    :type glass_id: list
    :rtype dict()  
    """
    workers = min(MAX_WORKER, len(glass_id))
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_gid = {executor.submit(
            query, g_id): g_id for g_id in sorted(glass_id)}
        result = {}
        for future in futures.as_completed(future_to_gid):
            g_id = future_to_gid[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (g_id, exc))
            else:
                print('%r glass_id has %d rows' % (g_id, len(data)))
            result.setdefault(g_id, data)
    return result
