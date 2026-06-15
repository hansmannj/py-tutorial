SHELL = /bin/bash

.DEFAULT_GOAL := help

# Find all Python files outside hidden directories
PYTHON_FILES := $(shell find ./* -type f -name "*.py" -print)

VENV := .venv
UV   := uv


all: help


.PHONY: help
help:
	@echo "Usage: make <target>"
	@echo
	@echo "Setup:"
	@echo "  setup          Create .venv and install all packages from requirements.txt"
	@echo
	@echo "Code quality:"
	@echo "  format         Format code with ruff (style only)"
	@echo "  lint           Lint code with ruff (report only, no fixes)"
	@echo "  format-lint    Format and fix all auto-fixable issues"
	@echo "  test           Run pytest on solutions/"
	@echo
	@echo "Cleanup:"
	@echo "  clean          Remove .venv and cached files"


.PHONY: setup
setup:
	$(UV) venv
	$(UV) pip install -r requirements.txt


.PHONY: format
format:
	$(UV) run ruff format $(PYTHON_FILES)


.PHONY: lint
lint:
	$(UV) run ruff check $(PYTHON_FILES)


.PHONY: format-lint
format-lint:
	$(UV) run ruff format $(PYTHON_FILES)
	$(UV) run ruff check --fix $(PYTHON_FILES)


.PHONY: test
test:
	$(UV) run pytest solutions/


.PHONY: clean
clean:
	rm -rf $(VENV) __pycache__ .pytest_cache .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
