FROM postgres:latest

# Copy migration scripts + data from intermediate image
ENV WORKDIR /opt/svc-events/migrations
COPY ./ ${WORKDIR}/

# Copy and prepare the entry point
RUN mv ${WORKDIR}/db-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/db-entrypoint.sh /
RUN chmod a+x db-entrypoint.sh

# Execute the entrypoint
ENTRYPOINT ["db-entrypoint.sh"]

# Run the DB server
CMD ["postgres"]
WORKDIR ${WORKDIR}
