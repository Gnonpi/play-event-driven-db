import psycopg2 as pg
from flask import current_app


def do_postgres_query(query, query_parameters):
    conn_params = {
        'host': current_app.config['POSTGRES_HOST'],
        'port': current_app.config['POSTGRES_PORT'],
        'dbname': current_app.config['POSTGRES_DB'],
        'user': current_app.config['POSTGRES_USER'],
        'password': current_app.config['POSTGRES_PASSWORD'],
    }
    with pg.connect(**conn_params) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, query_parameters)
            results = cursor.fetchall()
            return results
