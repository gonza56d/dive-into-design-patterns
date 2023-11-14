build:
	docker compose build

up:
	docker compose down
	docker compose up

debug:
	docker compose down
	docker compose up -d mongo
	docker compose run --rm --service-ports api
