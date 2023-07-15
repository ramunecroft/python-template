DIR_NAME := $(shell basename `pwd`)

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: format
format:  ## 🔧 format code
	isort .
	black .
	flake8 .
	mypy .
.PHONY: test
test:  ## 🧪 run test
	pytest tests/

.PHONY: run
dev:  ## run application
	DEVELOPMENT=TRUE uvicorn $(DIR_NAME).main:app --host 0.0.0.0 --port 8000 --reload
prod:
	PRODUCTION=TRUE uvicorn $(DIR_NAME).main:app --host 0.0.0.0 --port 8000 --reload


.PHONY: clean
clean:
	find . -type f -name "*.pyc" | xargs rm -fr
	find . -type d -name __pycache__ |xargs rm -fr


.PHONY: setup
setup: ## setup application
	poetry install
	poetry shell
	pre-commit install
