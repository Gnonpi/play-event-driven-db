-- Let's go with an online bank or something

CREATE SCHEMA online_bank;

CREATE TABLE online_bank.customer_event_type (
  id_customer_event_type SERIAL PRIMARY KEY,
  name_event VARCHAR(256) UNIQUE NOT NULL,
  description TEXT
);

CREATE TABLE online_bank.original_customer (
    id_customer SERIAL PRIMARY KEY,
    original_name VARCHAR(256) UNIQUE
);

INSERT INTO online_bank.customer_event_type(name_event) VALUES
    ('create_customer'),
    ('update_name'),
    ('update_balance');

CREATE TABLE online_bank.customer_event (
  id_customer_event SERIAL PRIMARY KEY,
  id_customer BIGINT REFERENCES online_bank.original_customer(id_customer),
  date_event TIMESTAMP WITH TIME ZONE DEFAULT now(),
  name VARCHAR(256),
  email VARCHAR(256),
  balance INTEGER
);
