# builder stage - install deps and build wheels
FROM python:3.8-slim as builder

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
# build wheels into /wheels to speed up final install
RUN pip wheel --wheel-dir /wheels -r /app/requirements.txt

# final stage - smaller runtime image
FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1 \
    PATH="/venv/bin:$PATH"

# runtime deps (keep minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    libjpeg62-turbo \
    && rm -rf /var/lib/apt/lists/*

# create non-root user
RUN useradd -m -U -s /bin/bash appuser

WORKDIR /app

# create venv and install wheels
RUN python -m venv /venv
COPY --from=builder /wheels /wheels
COPY --from=builder /app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --no-index --find-links=/wheels -r /app/requirements.txt

# copy source
COPY . /app

# create directory for static files (will be used by collectstatic)
RUN mkdir -p /app/staticfiles && chown -R appuser:appuser /app/staticfiles /app

# copy entrypoint and make executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER appuser

ENV DJANGO_SETTINGS_MODULE=yys_bio_django.settings
ENV PYTHONPATH=/app

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "yys_bio_django.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "1", "--log-level", "info"]
