FROM python:3.12-slim

RUN pip install --no-cache-dir poetry
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./

RUN poetry install --no-root --no-interaction --no-ansi --only main

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "rs_back.wsgi:application"]
