#!/bin/bash

#wait for Postgresql to be ready
echo "Waiting for postgresql....."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 1
done
echo "PostgresSQL started"


python manage.py migrate


python mange.py collectstatic --noinput

# Create a superuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(os.getenv('DJANGO_SUPERUSER_USERNAME'), os.getenv('DJANGO_SUPERUSER_EMAIL'), os.getenv('DJANGO_SUPERUSER_PASSWORD')) if not User.objects.filter(username=os.getenv('DJANGO_SUPERUSER_USERNAME')).exists() else print('Superuser already exists')" | python manage.py shell


python manage.py runserver 0.0.0.0:8000