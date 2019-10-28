from events.db_interactions import do_postgres_query

QUERY_CREATE_CUSTOMER = """
INSERT INTO online_bank.original_customer(original_name) 
VALUES ( %(original_name)s ) 
RETURNING id_customer;
"""

QUERY_UPDATE_BALANCE = """
INSERT INTO online_bank.customer_event(id_customer, balance)
VALUES ( %(id_customer)s, %(tx_balance)s )
RETURNING id_customer_event;
"""

QUERY_UPDATE_NAME = """
INSERT INTO online_bank.customer_event(id_customer, name)
VALUES ( %(id_customer)s, %(new_name)s )
RETURNING id_customer_event;
"""


def create_new_customer(name):
    id_customer = do_postgres_query(
        QUERY_CREATE_CUSTOMER,
        {'original_name': name}
    )
    update_customer_balance(id_customer, 0)
    update_customer_name(id_customer, name)
    return id_customer


def update_customer_balance(id_customer, tx_balance):
    id_event = do_postgres_query(
        QUERY_UPDATE_BALANCE,
        {'customer_id': id_customer, 'tx_balance': tx_balance}
    )
    return id_event


def update_customer_name(id_customer, new_name):
    id_event = do_postgres_query(
        QUERY_UPDATE_NAME,
        {'customer_id': id_customer, 'new_name': new_name}
    )
    return id_event
