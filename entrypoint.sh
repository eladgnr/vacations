#!/bin/sh
set -e

echo "Waiting for postgres at ${POSTGRES_HOST}:${POSTGRES_PORT}..."
python - <<'PYCODE'
import os, time, socket
host = os.getenv("POSTGRES_HOST", "db")
port = int(os.getenv("POSTGRES_PORT", "5432"))
for _ in range(120):
    try:
        with socket.create_connection((host, port), timeout=2):
            print("Postgres is up!")
            break
    except OSError:
        time.sleep(1)
else:
    raise SystemExit("Postgres not reachable")
PYCODE

echo "Applying migrations..."
python manage.py migrate --noinput

# Auto-create superuser if it doesn't exist
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
python - <<'PYCODE'
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
u = os.getenv("DJANGO_SUPERUSER_USERNAME")
p = os.getenv("DJANGO_SUPERUSER_PASSWORD")
e = os.getenv("DJANGO_SUPERUSER_EMAIL","")
if not User.objects.filter(username=u).exists():
    User.objects.create_superuser(username=u, password=p, email=e)
    print(f"Superuser '{u}' created")
else:
    print(f"Superuser '{u}' already exists")
PYCODE
fi

# Auto-load fixture if DB looks empty
python - <<'PYCODE'
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")
django.setup()
from vacations.models import Country
from django.core.management import call_command
if Country.objects.count() == 0:
    try:
        print("Loading initial data from data.json...")
        call_command('loaddata', 'data.json', verbosity=1)
        print("Initial data loaded.")
    except Exception as e:
        print(f"Fixture load skipped/failed: {e}")
else:
    print("Initial data not loaded (DB already has countries).")
PYCODE

# Collect static (safe in dev)
python manage.py collectstatic --noinput || true

echo "Starting Django dev server..."
exec python manage.py runserver 0.0.0.0:8000
