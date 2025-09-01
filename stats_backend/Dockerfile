FROM python:3.12-slim

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements from repo root
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy stats_backend project (manage.py + inner project folder)
COPY stats_backend /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
