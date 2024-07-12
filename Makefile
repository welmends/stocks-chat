.PHONY: run
run:
	docker-compose up -d --build

docker-prune:
	-@docker stop $(shell docker ps -aq)
	-@docker rm $(shell docker ps -aq)
	-@docker rmi $(shell docker images -q)
	-@docker volume rm $(shell docker volume ls -q)
	-@docker network prune -f
	-@docker system prune -a --volumes -f
	
dev:
	virtualenv .env -p python3.10
	pip install -r requirements.txt
	pre-commit clean
	pre-commit install