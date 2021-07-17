.PHONY: dev venv test pip-compile requirements install

VENV_NAME   = venv
PYTHON_BIN  = python3

all: dev test

dev: venv requirements

venv:
	$(PYTHON_BIN) -m venv $(VENV_NAME)

pip-upgrade:
	$(VENV_NAME)/bin/pip-compile -rU --generate-hashes requirements/requirements.ini

pip-compile:
	$(VENV_NAME)/bin/pip-compile -r --generate-hashes requirements/requirements.ini

requirements:
	$(VENV_NAME)/bin/pip install -r requirements/requirements.txt

install-tox:
	$(VENV_NAME)/bin/pip install tox

test:
	TOX_PARALLEL_NO_SPINNER=1 $(VENV_NAME)/bin/tox -p

test-refresh:
	TOX_PARALLEL_NO_SPINNER=1 $(VENV_NAME)/bin/tox -rp

black:
	$(VENV_NAME)/bin/black ./

