PYTHON_VERSION = 3.10.0

default: run

init: install-deps

install-deps:
	@pip install --upgrade pip setuptools wheel
	@pip install --upgrade poetry
	@poetry install
	@pre-commit install
	@pre-commit run --all-files

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