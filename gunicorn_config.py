# gunicorn_config.py
worker_class = 'gevent'
workers = 1  # Ajusta el número según las necesidades de tu aplicación
bind = '0.0.0.0:5000'
