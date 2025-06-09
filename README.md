# Widget API

A simple FastAPI-based CRUD REST API for managing Widgets.

## Requirements

- Python 3.8+
- pip

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Usage

- Visit: `http://127.0.0.1:8000/docs` for Swagger UI.
- Use `/widgets/` endpoints for CRUD operations.

## Testing

```bash
pytest test_main.py
```

## Linting & Security

```bash
flake8 .
bandit -r .
```
