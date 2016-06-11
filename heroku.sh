sh init.sh
python manage.py migrate

gunicorn --pythonpath app A2A.wsgi --log-file -
