.PHONY: test
test:
	pytest -x hyperform tests

.PHONY: lint
lint:
	flake8 --config=setup.cfg hyperform tests

.PHONY: coverage
coverage:
	pytest --cov-report html --cov hyperform hyperform tests

.PHONY: install
install:
	pip install -e .[test,dev]
	pre-commit install --hook-type pre-push
