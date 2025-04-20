.PHONY: doc build unit test dev install clean

doc:
	@echo "📚 Building Sphinx docs..."
	@if [ ! -d docs ]; then \
		echo "🛠️  'docs/' folder not found. Running sphinx-quickstart..."; \
		mkdir -p docs && \
		sphinx-quickstart -q -p "file_publisher" -a "Taiseem Dadwal" --sep --makefile docs; \
	fi
	@cd docs && make html
	@echo "📚 Sphinx docs built successfully. Open docs/_build/html/index.html to view."
build:
	@echo "📦 Building wheel and sdist..."
	@. .venv/bin/activate && \
	which python && \
	python -m build || echo "❌ 'build' module not found. Run 'pip install build' inside your venv."
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
