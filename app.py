import os
from flask import Flask, url_for
from flask import request, redirect

import pprint
import psycopg2 as pg

from appcontent.queries import QUERY_GET_TRANSACTIONS, QUERY_INSERT_TRANSACTION
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv('.env')
DSN_CONFIG = {
    'host': os.getenv('dbhost'),
    'port': os.getenv('dbport'),
    'dbname': os.getenv('dbname'),
    'user': os.getenv('dbuser'),
    'password': os.getenv('dbpassword')
}


def run_query(query, params=None, return_results=False):
    with pg.connect(**DSN_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            if return_results:
                return cursor.fetchall()


@app.route('/')
def home():
    return redirect(url_for('get_transactions'))


@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = run_query(QUERY_GET_TRANSACTIONS, return_results=True)
    json_pprint = pprint.pformat(transactions)
    return json_pprint

# @app.route('/create-user', method=['POST'])
# def


@app.route('/send-transaction', methods=['POST'])
def send_transaction():
    if request.method == 'POST':
        data_transaction = request.get_json()
        # TODO: put schema verification here
        payload = {
            'name': data_transaction['name'],
            'sent_amount': data_transaction['sent_amount']
        }
        run_query(QUERY_INSERT_TRANSACTION, params=payload)
    else:
        return redirect(url_for('get_transactions'))


if __name__ == '__main__':
    app.run(host='localhost',
            port=8686,
            debug=True)
