FROM python:3.10-slim-bullseye

WORKDIR /opt/fran

COPY ./entrypoint_fail.py ./

COPY ./entrypoint_success.py ./

#RUN python3 entrypoint_fail.py


