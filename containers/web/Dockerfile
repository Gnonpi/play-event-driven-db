FROM python:3.6

ENV WORKDIR /opt/svc-events
RUN mkdir -p ${WORKDIR}/
COPY poetry.lock pyproject.toml run_app.py ${WORKDIR}/
COPY events/ ${WORKDIR}/events/

RUN cd ${WORKDIR} && \
    pip3 install --upgrade pip && \
    pip3 install poetry && \
    poetry install --no-dev

EXPOSE 8000
WORKDIR ${WORKDIR}
CMD ["poetry", "run", "gunicorn", "-b", ":8000", "run_app"]
