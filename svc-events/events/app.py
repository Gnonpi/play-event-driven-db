from flask import Flask, Blueprint, request, jsonify

from events.customer_db import create_new_customer, update_customer_balance

model_blue = Blueprint('model_blue', __name__)


@model_blue.route(rule='/create-customer', methods=['PUT'])
def route_create_customer():
    input_json = request.json
    # TODO: add data validation
    id_customer = create_new_customer(input_json['name'])
    return jsonify({'data': {
        'status': 'success',
        'id_customer': id_customer
    }}), 200


@model_blue.route(rule='/update-balance', methods=['POST'])
def route_update_balance():
    input_json = request.json
    # TODO: add data validation
    customer_id = input_json['customer_id']
    tx_balance = input_json['tx_balance']
    id_event = update_customer_balance(customer_id, tx_balance)
    return jsonify({'data': {
        'status': 'success',
        'id_event': id_event
    }})


def create_app():
    app = Flask(__name__)
    app.config.from_object('events.config.Config')

    @app.route(rule='/hello')
    def route_hello():
        app.logger.debug('Hello route!')
        return 'Hello!', 200

    app.register_blueprint(model_blue)

    return app
