FROM python:3.8-slim

COPY . /app

WORKDIR /app

RUN pip3 install -r app/requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--config", "gunicorn_config.py", "app.wsgi:app"]