python -m manage makemigrations
python -m manage migrate
gunicorn pyatiletka.wsgi:application --bind 0.0.0.0:8000
