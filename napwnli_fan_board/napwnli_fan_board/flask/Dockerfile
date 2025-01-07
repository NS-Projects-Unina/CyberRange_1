FROM python:latest

WORKDIR /app

RUN pip install --no-cache-dir Flask
RUN pip install --no-cache-dir Flask-MySQLdb
EXPOSE 5000

CMD ["python", "app.py"]