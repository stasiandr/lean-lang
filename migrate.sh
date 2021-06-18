#/bin/sh

docker-compose run backend python manage.py makemigrations
docker-compose run backend python manage.py migrate
