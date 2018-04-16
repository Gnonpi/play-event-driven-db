DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS customer_transactions;

CREATE TABLE customers (
    id_customer SERIAL PRIMARY KEY,
    name TEXT,
    amount FLOAT
);


CREATE TABLE customer_transactions (
    id_transaction SERIAL PRIMARY KEY,
    id_sender BIGINT REFERENCES customers(id_customer),
    sent_amount FLOAT NOT NULL CHECK (sent_amount > 0)
);

