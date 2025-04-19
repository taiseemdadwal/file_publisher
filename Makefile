.PHONY: doc build unit test dev install clean

doc:
	@echo "Building Sphinx docs..."
	cd docs && make html

build:
	@echo "Building wheel and sdist..."
	python -m build

unit:
	@echo "Running unit tests..."
	pytest

test:
	@echo "Running tox for multi-version tests..."
	tox

dev:
	@echo "Setting up development environment in .venv..."
	python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -e .[dev]
	@echo "✅ Done. To activate the virtual environment, run:"
	@echo "   source .venv/bin/activate"

install:
	@echo "Installing wheel..."
	pip install dist/*.whl

clean:
	@echo "Cleaning build, dist, .pyc, cache, tox, and docs/_build..."
	rm -rf build dist .eggs *.egg-info
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf .tox
	rm -rf .venv
	rm -rf docs/_build
