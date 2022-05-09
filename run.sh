#!/bin/bash

DJANGO_TEST=true # TODO: Change to dotenv file.
DJANGO_LOGS=true # TODO: Change to dotenv file.


if [ $DJANGO_TEST == "true" ]; then
    printf "\nStart Testing....\n"
    printf "\nDown containers\n\n"
    docker-compose down
    printf "\nStart build\n\n"
    docker-compose -f docker-compose.tests.yml up --build --remove-orphans -d
    printf "\nStart db migration\n\n"
    docker exec django_test python manage.py migrate
    # docker exec django-test python -Wa manage.py test
else
    printf "\nDown old container\n\n"
    docker-compose down
    printf "\nStart build\n\n"
    docker-compose up --build --remove-orphans -d
    printf "\nStart db migration\n\n"
    docker exec django python manage.py migrate

    # Auto logs
    if [ $DJANGO_LOGS == "true" ]; then
        echo "DJANGO_LOGS: $DJANGO_LOGS"
        reset
        docker logs -f django
    else
        echo "DJANGO_LOGS: $DJANGO_LOGS"
    fi
fi

