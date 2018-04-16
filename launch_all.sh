#!/usr/bin/env bash

# Installing dependencies
# pipenv install

# Extract variables from .env file
. '.env'

# Launch the DB creation
PGPASSWORD=$dbpassword psql -h $dbhost -p $dbport -U $dbuser -d $dbname -f database/create-db.sql

# Launch server with Gunicorn ( don't use Flask server )
gunicorn -b 127.0.0.1:8686 -w 2 app:app