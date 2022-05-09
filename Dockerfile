FROM python:3.9.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app/

RUN pip install pip -U
RUN pip install -r requirements.txt