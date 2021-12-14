.PHONY: default
        .DEFAULT_GOAL := help
default: build

ifndef VERBOSE
        .SILENT:
endif


VENV_PATH ?= venv
VENV_ACTIVATE = . $(VENV_PATH)/bin/activate

.PHONY: run

run:

	$(VENV_ACTIVATE) && python manage.py runserver
