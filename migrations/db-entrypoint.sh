#!/bin/bash -e

# Copy migration scripts to DB initialization storage
cp ${WORKDIR}/*.sql /docker-entrypoint-initdb.d

# Running the app (or whatever is send via command) through docker-entrypoint.sh from postgres image
/usr/local/bin/docker-entrypoint.sh "$@"
