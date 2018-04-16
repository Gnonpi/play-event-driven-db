QUERY_GET_TRANSACTIONS = """
    SELECT
        cus_tra.time_sent,
        cus.name,
        cus_tra.sent_amount
    FROM
        event_driven.customer cus,
        event_driven.customer_transaction cus_tra
    WHERE
        cus.id_customer=cus_tra.id_sender
    ORDER BY time_sent;        
"""

QUERY_INSERT_TRANSACTION = """
    INSERT INTO event_driven.customer_transaction (id_customer, sent_amount)
        VALUES (
            SELECT id_customer FROM event_driven.customer WHERE name=%(name)s,
            %(sent_amount)s
        );
    UPDATE
        event_driven.customer
    SET 
        amount= amount - %(sent_amount)s
    WHERE
        name=%(name)s;
"""

QUERY_CREATE_CUSTOMER = """
    INSERT INTO event_driven.customer (name, amount) 
        VALUES (%(name)s, %(amount)s);
"""