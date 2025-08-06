lint:
	@echo
	ruff format .
	@echo
	ruff check --silent --exit-zero --fix .
	@echo
	ruff check .
	@echo
	mypy .

local/start:
	uvicorn src.main:app --port 8008 --reload