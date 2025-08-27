# stats_site/Dockerfile
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# only need pg client for pg_isready
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD sh -c 'HOST="${POSTGRES_HOST:-${DB_HOST:-db}}"; \
    PORT="${POSTGRES_PORT:-${DB_PORT:-5432}}"; \
    USER="${POSTGRES_USER:-admin}"; \
    DB="${POSTGRES_DB:-vacations_db}"; \
    until pg_isready -h "$HOST" -p "$PORT" -U "$USER" -d "$DB"; do echo "Waiting for db $DB at $HOST:$PORT..."; sleep 1; done; \
    python manage.py migrate --noinput && \
    python manage.py runserver 0.0.0.0:8000'
