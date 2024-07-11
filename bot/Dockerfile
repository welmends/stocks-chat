FROM python:3.10-slim

LABEL maintainer="Wellington Mendes - wellmend0@gmail.com"

WORKDIR /bot

COPY bot/ /bot
COPY config.yml /bot

RUN pip install -r /bot/requirements.txt

CMD ["python3", "-u", "stock_bot.py"]