ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-bookworm as builder

# Make sure that my environment will be as isolated as possible and above
# all that my installation will not mess up with the system Python.
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
COPY README.md /app

RUN pip install poetry==1.5.1

# Install the project's dependencies in the virtual environment and cache the virtual environment.
# Leverage a cache mount to /tmp/poetry_cache to speed up subsequent builds.
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --no-root

FROM python:${PYTHON_VERSION}-slim-bookworm as runtime

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Use the virtual environment.
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

# Copy the virtual environment from the builder stage.
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /app

# Copy the source code into the container.
COPY python_template/ /app/python_template
COPY tests /app/tests
COPY docs /app/docs

# Make log directory with appuser privilege
RUN mkdir /app/logs/ && \
    chown appuser:appuser /app/logs/ && \
    chmod 755 /app/logs/


# Expose the port that the application listens on.
EXPOSE 8000

# Switch to the non-privileged user to run the application.
USER appuser

# Run the application.
ENTRYPOINT ["uvicorn", "python_template.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]