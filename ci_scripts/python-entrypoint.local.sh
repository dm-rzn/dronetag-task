#!/bin/sh
echo "Starting migrate"
python manage.py migrate
echo "Create static files"
python manage.py collectstatic --no-input
echo "Create cache tables"
python manage.py createcachetable
echo "Create superuser"
python manage.py create_superuser_init
echo "Starting runserver (gunicorn)"
gunicorn flight_analysis.wsgi:application --bind 0.0.0.0:8000 --workers=5 --reload
