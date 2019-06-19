SHELL := /bin/bash
setup:
	python3 -m venv venv && source ./venv/bin/activate && pip install -r requirements.txt

test:
	PYTHONPATH=src pytest --random-order

cov:
	PYTHONPATH=src pytest --cov-report html --cov=src tests/