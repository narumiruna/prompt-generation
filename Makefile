install:
	uv sync

lint:
	uv run ruff check .

type:
	uv run mypy --install-types --non-interactive .

test:
	uv run pytest -v -s --cov=. tests

cover:
	uv run pytest -v -s --cov=. --cov-report=xml tests

publish:
	uv build wheel
	uv publish

.PHONY: lint test publish
