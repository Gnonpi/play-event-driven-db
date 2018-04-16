import os
import requests
import time
from dotenv import load_dotenv
from faker import Faker

fake = Faker()

load_dotenv('.env')
BASE_URL = 'http://' + os.getenv('hostserver') + ':' + os.getenv('hostport')


def create_customers():
    payload = {
        'name': fake.name(),
        'amount': fake.random.randint(1, 20)
    }
    requests.post(BASE_URL + '/create-customer', json=payload)


def get_state_info():
    resp = requests.get(BASE_URL + '/transactions')
    if resp.status_code == 500:
        time.sleep(0.5)
        resp = requests.get(BASE_URL + '/transactions')
    return resp.json()
    # return requests.get(BASE_URL + '/transactions').json()


def create_transaction():
    state_info = get_state_info()
    payload = {
        'name': fake.random.choice(state_info)['name'],
        'sent_amount': fake.random.randint(0, 2)
    }
    requests.post(BASE_URL + '/send-transaction', json=payload)


def delete_transaction():
    state_info = get_state_info()
    payload = {
        'id_transaction': fake.random.choice(state_info)['id_transaction'],
    }
    requests.post(BASE_URL + '/delete-transaction', json=payload)


def delete_customer():
    state_info = get_state_info()
    payload = {
        'id_customer': fake.random.choice(state_info)['id_customer'],
    }
    requests.post(BASE_URL + '/delete-transaction', json=payload)


def one_loop():
    MAX_LOOP = 10000
    rand_val = fake.random.random()
    if rand_val > 0.3:
        create_transaction()
    elif rand_val > 0.1:
        delete_transaction()
    else:
        delete_customer()

    stop_loop = fake.random.randint(0, MAX_LOOP) == MAX_LOOP
    time.sleep(fake.random.uniform(0.5, 2.))
    return stop_loop


if __name__ == '__main__':
    for _ in range(3):
        create_customers()
    stop_loop = False
    while not stop_loop:
        stop_loop = one_loop()
