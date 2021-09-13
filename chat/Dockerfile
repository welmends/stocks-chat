FROM python:3.8-slim

LABEL maintainer="Wellington Mendes - wellmend0@gmail.com"

RUN pip install Django
RUN pip install djangorestframework
RUN pip install PyYAML
RUN pip install pika

WORKDIR /chat

COPY chat/ /chat
COPY config.yml /chat

RUN rm -rf /chat/db.sqlite3
RUN python3 manage.py migrate

CMD ["python3", "-u", "manage.py", "runserver", "0.0.0.0:8000"]