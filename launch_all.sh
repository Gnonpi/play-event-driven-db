#!/usr/bin/env bash

# Installing dependencies
pipenv install

# Extract variables from .env file
. '.env'

# Launch the DB creation
PGPASSWORD=$dbpassword psql -h $dbhost -p $dbport -U $dbuser -d $dbname -1 -f database/create-db.sql

# Launch server with Gunicorn ( don't use Flask server )
gunicorn -w 4 app:app