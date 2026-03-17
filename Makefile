PYTHON ?= python3
VENV ?= .venv
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest
RUFF = $(VENV)/bin/ruff
PLAYWRIGHT = $(VENV)/bin/playwright

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PLAYWRIGHT) install --with-deps chromium

lint:
	$(RUFF) check .

test:
	$(PYTEST)

run:
	$(VENV)/bin/python app/app.py
