# Polygon INFO project
## Installation
- `poetry install` - install dependencies
- `poetry shell` - activate venv

## Run
- `python src/manage.py runserver` - dev server

## Urls
- `http://localhost:8000/get_balance?address=`
- `http://localhost:8000/get_balance_batch` with json body `{"addresses": []}`
- `http://localhost:8000/top?n=`
- `http://localhost:8000/get_token_info?token_address=`