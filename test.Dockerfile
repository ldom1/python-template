FROM python:3.10-bookworm as builder

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY README.md ./

RUN pip install poetry==1.5.1

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --no-root

FROM python:3.10-slim-bookworm as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY python_template/ /app/python_template
COPY tests /app/tests
COPY docs /app/docs

WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["uvicorn", "python_template.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]