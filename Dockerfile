FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app/

RUN pip install pip -U ; pip install -r requirements.txt

EXPOSE 8000