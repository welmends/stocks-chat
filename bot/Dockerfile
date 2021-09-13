FROM python:3.8-slim

LABEL maintainer="Wellington Mendes - wellmend0@gmail.com"

RUN pip install PyYAML
RUN pip install pika
RUN pip install pyrabbit
RUN pip install requests

WORKDIR /bot

COPY bot/ ./
COPY config.yml ./

CMD ["python3", "-u", "stock_bot.py"]