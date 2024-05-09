all: build down up

pull:
	docker-compose pull

push:
	docker-compose push

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

dev:
	docker-compose run --volume=${PWD}/src:/src --publish=8000:8000 app bash -c 'uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload'


poetry_add:
	docker-compose run --rm --no-deps --volume=${PWD}:${PWD} --workdir=${PWD} app poetry add $p
	sudo chown -R ${USER} ./poetry.lock ./pyproject.toml

poetry_lock:
	docker-compose run --rm --no-deps --volume=${PWD}:${PWD} --workdir=${PWD} app poetry lock --no-update
	sudo chown -R ${USER} ./poetry.lock


.PHONY: all pull push build up down dev poetry_add poetry_lock
