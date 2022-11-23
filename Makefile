PYTHON_VERSION = 3.10.0

default: run

init: install-deps

install-deps:
	@pip install --upgrade pip setuptools wheel
	@pip install --upgrade poetry
	@poetry install
	@pre-commit install
	@pre-commit run --all-files

poetry-export:
	@poetry export --with dev -vv --no-ansi --no-interaction --without-hashes --format requirements.txt --output requirements.txt

lock-deps:
	@poetry lock -vv --no-ansi --no-interaction

.PHONY: isort
isort:
	@poetry run isort --sp pyproject.toml .

.PHONY: isort-check
isort-check:
	@poetry run isort --check --sp pyproject.toml .

.PHONY: flake8
flake8:
	@poetry run flake8 .

.PHONY: blue
blue:
	@poetry run blue -v .

.PHONY: blue-check
blue-check:
	@poetry run blue -v --check .

.PHONY: format
format: blue isort

.PHONY: lint
lint: isort-check flake8 blue-check

run:
	@poetry install
	@poetry run env $(shell grep -v ^\# .env | xargs) uvicorn src.main:app --reload --port 8080

build-container:
	@docker build \
		--tag ranog:url-shortener \
		--build-arg GIT_HASH=$(shell git rev-parse HEAD) \
		.

run-container: poetry-export build-container
	@docker run --rm -it \
		-v $(HOME)/.config/gcloud/application_default_credentials.json:/gcp/creds.json:ro \
		--name ranog_url-shortener \
		--env-file .env \
		--env PORT=8080 \
		--env GOOGLE_APPLICATION_CREDENTIALS=/gcp/creds.json \
		--publish 8080:8080 \
		ranog:url-shortener

test-all:
	@poetry run env $(shell grep -v ^\# .env | xargs) pytest
