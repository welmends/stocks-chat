FROM python:3.10-slim

LABEL maintainer="Wellington Mendes - wellmend0@gmail.com"

WORKDIR /chat

COPY chat/ /chat
COPY config.yml /chat

RUN pip install -r /chat/requirements.txt

RUN rm -rf /chat/db.sqlite3
RUN python3 manage.py migrate

CMD ["python3", "-u", "manage.py", "runserver", "0.0.0.0:8000"]