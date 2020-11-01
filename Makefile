clean:
	find . -name "*.py[co]" -exec rm --force {} +
	find . -name "__pycache__" -exec rm -r --force {} +
	find . -name ".pytest_cache" -exec rm -r --force {} +
	find . -name ".mypy_cache" -exec rm -r --force {} +

test:
	pytest

lint:
	flake8
	mypy ./
	black ./ --check
