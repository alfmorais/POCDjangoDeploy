close:
	@echo "--> Close Docker."
	docker-compose down

run:
	@echo "--> Running Docker."
	SHOW_DEBUG_TOOLBAR=0 docker-compose up

createsuperuser:
	@echo "--> Creating superuser on Docker."
	docker-compose run --rm api python api/manage.py createsuperuser

makemigrations:
	@echo "--> Creating migrations on Docker."
	docker-compose run --rm api python api/manage.py makemigrations $(name)

migrate:
	@echo "--> Running migrations on Docker."
	docker-compose run --rm api python api/manage.py migrate

build:
	@echo "--> Building Docker Base Image"
	DOCKER_BUILDKIT=1 docker build -f Dockerfile .
	@echo "--> Building Compose"
	DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose build

bash:
	docker-compose run --rm api bash

test:
	@echo "--> Testing on Docker."
	docker-compose run --rm api pytest --cov-fail-under 97 --cov-report term-missing $(path)

