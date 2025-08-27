Django Elad Vacation Site Project
---------------------------------

Project Overview
----------------
This project is a Django web app for managing vacations, users, and countries, with admin and user roles and a REST API.
It includes a Docker setup that starts:
- PostgreSQL (db)
- Main Django site (web)
- Separate Django **statistics** site (stats) that connects to the same DB and exposes a simple dashboard + API.

Stack
-----
- Backend/Frontend: Python/Django (server-rendered templates + DRF)
- Database: PostgreSQL
- Orchestration: Docker Compose

Admin Credentials (dev/test)
----------------------------
- Username: root
- Email:    root@email.com
- Password: admin

Environment (.env)
------------------
Make sure the file `.env` exists in the project root with:
POSTGRES_DB=vacations_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=1234
POSTGRES_HOST=db
POSTGRES_PORT=5432

DJANGO_DEBUG=1
DJANGO_SECRET_KEY=dev-insecure-key-change-me
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

Auto superuser:
DJANGO_SUPERUSER_USERNAME=root
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=root@email.com

Project URLs
------------
Main site:
- Homepage:  http://127.0.0.1:8000/
- Admin:     http://127.0.0.1:8000/admin
- API:       http://127.0.0.1:8000/api/vacations/

Statistics site:
- Dashboard: http://127.0.0.1:8001/
- API:       http://127.0.0.1:8001/api/vacations-per-country/

Quick Start (Docker)
--------------------
1) Ensure these files exist in the project root:
   - `.env`
   - `docker-compose.yml`
   - `Dockerfile` (main web)
   - `entrypoint.sh` (LF line endings, if used)
   - `requirements.txt`
   - `data.json` (fixture)
   - `media/` (images referenced by data.json)
   - `stats_site/` (contains the separate Django stats project + its Dockerfile)

2) Start everything (build if needed):
   PowerShell:
     docker compose up -d --build
   (Tip: PowerShell doesn’t support `&&`. Run commands on separate lines or use `;`.)

3) Check services:
   - docker compose ps
   - docker compose logs -f web
   - docker compose logs -f stats

Behavior on first run:
- The DB container starts and becomes healthy.
- The main Django app runs migrations, ensures superuser (root/admin), and auto-loads `data.json` if the DB is empty.
- The stats app connects to the same DB and serves a dashboard + API.

Common Commands
---------------
- Start (foreground):              docker compose up --build
- Start (detached):                docker compose up -d --build
- See running services:            docker compose ps
- Tail logs:                       docker compose logs -f web
                                   docker compose logs -f stats
                                   docker compose logs -f db
- Exec into Django (main):         docker compose exec web bash
- Exec into Django (stats):        docker compose exec stats bash
- Stop all:                        docker compose down
- Stop & remove volumes (reset):   docker compose down -v

Notes
-----
- The database persists in the `db_data` volume.
- `data.json` is loaded automatically only when the DB is empty (first run).
- Media is served from the host `./media` folder (bind-mounted).
- `STATIC_ROOT` is set so `collectstatic` won’t error (and `static_data` volume is mapped).
- Both web and stats wait for Postgres before starting.
- If port 8000 is busy on your host, change the mapping in docker-compose (e.g., "8002:8000") and browse http://127.0.0.1:8002/.

Troubleshooting
---------------
- If http://127.0.0.1:8000/ doesn’t open:
  1) Start the web service:       docker compose up -d web
  2) Check logs:                  docker compose logs -f web
  3) Confirm ports aren’t in use: change host mapping if needed.
- If stats site builds fail with psycopg errors on Python 3.13:
  - Use psycopg 3 binaries:       in stats_site/requirements.txt set `psycopg[binary]==3.2.9`
- PowerShell tip: don’t use `&&`; run commands on separate lines or use `;`.

Users
-----
Admin user:
- username: root
- password: admin

Regular user:
- username: amos
- password: 1234

Project URLs
------------
### 🌍 Vacations Site (`http://127.0.0.1:8000`)
- **Homepage**:                  http://127.0.0.1:8000/
- **Admin**:                     http://127.0.0.1:8000/admin/
- **Login / Register**:           http://127.0.0.1:8000/accounts/login/  
                                  http://127.0.0.1:8000/register/
- **Country detail**:             http://127.0.0.1:8000/country/<country_name>/
- **Edit vacation (admin)**:      http://127.0.0.1:8000/vacation/<id>/edit/
- **Choose vacation (book)**:     http://127.0.0.1:8000/vacation/<id>/choose/
- **My vacations**:               http://127.0.0.1:8000/my-vacations/
- **Like vacation**:              http://127.0.0.1:8000/vacations/<id>/like/
- **Delete vacation (admin)**:    http://127.0.0.1:8000/vacation/delete/<id>/
- **Order vacation**:             http://127.0.0.1:8000/vacation/order/<id>/
- **Add vacation (admin)**:       http://127.0.0.1:8000/add-vacation/

#### 📡 Vacations API
- **Vacations stats**:            http://127.0.0.1:8000/api/vacations/stats/
- **Total users**:                http://127.0.0.1:8000/api/users/total/
- **Total likes**:                http://127.0.0.1:8000/api/likes/total/
- **Likes distribution (per vacation)**:  
                                   http://127.0.0.1:8000/api/likes/distribution/
- **Vacations per country**:      http://127.0.0.1:8000/api/vacations-per-country/
- **Likes per country**:          http://127.0.0.1:8000/api/likes-per-country/
- **Vacations list (DRF)**:       http://127.0.0.1:8000/api/vacations/
- **Vacation detail (DRF)**:      http://127.0.0.1:8000/api/vacations/<id>/

---

### 📊 Stats Site (`http://127.0.0.1:8001`)
- **Dashboard (requires login)**: http://127.0.0.1:8001/
- **Login**:                      http://127.0.0.1:8001/stats-login/
- **Logout** (POST form):         http://127.0.0.1:8001/logout/

