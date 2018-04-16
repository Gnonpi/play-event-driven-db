DROP SCHEMA IF EXISTS event_driven CASCADE;
CREATE SCHEMA event_driven;
ALTER DATABASE :DBNAME SET search_path = "$user", event_driven;

DROP TABLE IF EXISTS event_driven.customer_transaction;
DROP TABLE IF EXISTS event_driven.customer;

CREATE TABLE event_driven.customer (
    id_customer SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    amount FLOAT
);


CREATE TABLE event_driven.customer_transaction (
    id_transaction SERIAL PRIMARY KEY,
    id_sender BIGINT NOT NULL REFERENCES event_driven.customer(id_customer),
    sent_amount FLOAT NOT NULL CHECK (sent_amount > 0),
    time_sent TIMESTAMP WITHOUT TIME ZONE DEFAULT (now() at time zone 'utc')
);

INSERT INTO event_driven.customer (name, amount) VALUES ('David', 20.);
INSERT INTO event_driven.customer_transaction (id_sender, sent_amount)
    SELECT
        id_customer,
        1.
    FROM
        event_driven.customer
    WHERE
        name='David';

