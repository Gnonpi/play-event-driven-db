import os
from flask import Flask, url_for, jsonify
from flask import request, redirect

import psycopg2 as pg
from psycopg2.extras import RealDictCursor

from appcontent.queries import QUERY_GET_TRANSACTIONS, QUERY_INSERT_TRANSACTION, QUERY_CREATE_CUSTOMER, \
    QUERY_DELETE_TRANSACTION, QUERY_DELETE_CUSTOMER
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
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            conn.commit()
            for note in conn.notices:
                print(note)
            if return_results:
                return cursor.fetchall()


@app.route('/')
def home():
    return redirect(url_for('get_transactions'))


@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = run_query(QUERY_GET_TRANSACTIONS, return_results=True)
    return jsonify(transactions) or ['NO TRANSACTIONS']


@app.route('/create-customer', methods=['POST'])
def create_customer():
    if request.method == 'POST':
        data_customer = request.get_json()
        # TODO: put schema verification here
        payload = {
            'name': data_customer['name'],
            'amount': data_customer['amount']
        }
        run_query(QUERY_CREATE_CUSTOMER, params=payload)
        return 'OK'
    else:
        return redirect(url_for('get_transactions'))


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
        return 'OK'
    else:
        return redirect(url_for('get_transactions'))


@app.route('/delete-transaction', methods=['DELETE'])
def delete_transaction():
    if request.method == 'DELETE':
        data_transaction = request.get_json()
        # TODO: put schema verification here
        payload = {
            'id_transaction': data_transaction['id_transaction']
        }
        run_query(QUERY_DELETE_TRANSACTION, params=payload)
        return 'OK'
    else:
        return redirect(url_for('get_transactions'))


@app.route('/delete-customer', methods=['DELETE'])
def delete_customer():
    if request.method == 'DELETE':
        data_transaction = request.get_json()
        # TODO: put schema verification here
        payload = {
            'id_customer': data_transaction['id_customer']
        }
        run_query(QUERY_DELETE_CUSTOMER, params=payload)
        return 'OK'
    else:
        return redirect(url_for('get_transactions'))


if __name__ == '__main__':
    app.run(host='localhost',
            port=8686,
            debug=True)
