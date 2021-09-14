# Stocks Chat

Stocks Chat is a simple browsed-based chat application that allow users to talk and to get stock quotes using bot commands.

## Completed All Mandatory and Bonus Features

- [x] Allow registered users to log in and talk with other users in a chatroom. 
- [x] Allow users to post messages as commands into the chatroom with the following format **/stock=stock_code**
- [x] Create a **decoupled** bot that will call an API using the stock_code as a parameter (https://stooq.com/q/l/?s=aapl.us&f=sd2t2ohlcv&h&e=csv, here _aapl.us_ is the stock_code)
- [x] The bot should parse the received CSV file and then it should send a message back into the chatroom using a message broker like RabbitMQ. The message will be a stock quote using the following format: “APPL.US quote is $93.42 per share”. The post owner will be the bot.
- [x] Have the chat messages ordered by their timestamps and show only the last 50 messages.
- [x] Unit test the functionality you prefer.
- [x] (BONUS) Have more than one chatroom.
- [x] (BONUS) Handle messages that are not understood or any exceptions raised within the bot.
- [x] (OTHER) Put all services in containers.
- [x] (OTHER) Use Github's Kanban.
- [x] (OTHER) Use RabbitMQ as Message Broker for Bot commands/responses communication.

## Deployment

You can deploy all the project with Docker. Type the following command:

```
docker-compose up -d --build
```

After the containers creation you can checkout the web application at http://localhost:8000.

## Usage

Admin user credentials:
- username: admin
- password: admin

Default user credentials:
- username: user
- password: 123

## Testing

You can unit testing some features. Type the following commands after the deployment:

```
docker exec -it chat bash
python3 manage.py test
```

This must process several unit tests.

## Screens

<img width="1440" alt="login" src="https://user-images.githubusercontent.com/19287934/133186126-62a2a946-ce21-4d09-a705-b5486ae6185f.png">

<img width="1440" alt="rooms" src="https://user-images.githubusercontent.com/19287934/133186298-5b07a5f7-ecef-448a-82a3-d53dab78bffd.png">

<img width="1440" alt="chat" src="https://user-images.githubusercontent.com/19287934/133186322-2461c500-7187-40ba-915e-6d82d80c7a09.png">



