Django Elad Vacation Site Project
---------------------------------

Project Overview
----------------
This is a full-stack Django project for managing **vacations, users, likes, and countries**, with role-based access (admin & user), booking system, and REST API.  

It also includes:
- A **main Django site** (vacations web app)  
- A separate **statistics site** (Django) for dashboards (vacations per country, overdue vacations, likes, etc.)  
- Shared **PostgreSQL** database  

Both apps are containerized and orchestrated with **Docker Compose**.

Stack
-----
- Backend: Python, Django, Django REST Framework
- Frontend: Django templates (Bootstrap 5), custom HTML/CSS
- Database: PostgreSQL
- Orchestration: Docker Compose

Admin Credentials (dev/test)
----------------------------
- Username: `root`  
- Email:    `root@email.com`  
- Password: `admin`  

Environment (.env)
------------------
`.env` file in project root must include:


POSTGRES_DB=vacations_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=1234
POSTGRES_HOST=db
POSTGRES_PORT=5432

DJANGO_DEBUG=1
DJANGO_SECRET_KEY=dev-insecure-key-change-me
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

Auto superuser on first run

DJANGO_SUPERUSER_USERNAME=root
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=root@email.com


Project URLs
------------
### 🌍 Vacations Site (`http://127.0.0.1:8000`)
- **Homepage**:                  http://127.0.0.1:8000/
- **About Page**:                http://127.0.0.1:8000/about/  (with custom banner image + back to home button)
- **Admin Panel**:               http://127.0.0.1:8000/admin/
- **Login / Register**:          http://127.0.0.1:8000/accounts/login/  
                                 http://127.0.0.1:8000/register/
- **Country detail**:            http://127.0.0.1:8000/country/<country_name>/
- **Choose vacation (book)**:    http://127.0.0.1:8000/vacation/<id>/choose/
- **My vacations**:              http://127.0.0.1:8000/my-vacations/
- **Like vacation**:             http://127.0.0.1:8000/vacations/<id>/like/
- **Order vacation**:            http://127.0.0.1:8000/vacation/order/<id>/
- **Add vacation (admin)**:      http://127.0.0.1:8000/add-vacation/
- **Edit / Delete vacation (admin)**: http://127.0.0.1:8000/vacation/<id>/edit/ , delete/

#### 📡 Vacations API
- **Vacations list (DRF)**:       http://127.0.0.1:8000/api/vacations/
- **Vacation detail (DRF)**:      http://127.0.0.1:8000/api/vacations/<id>/
- **Vacations per country**:      http://127.0.0.1:8000/api/vacations-per-country/
- **Total likes**:                http://127.0.0.1:8000/api/likes/total/
- **Likes per country**:          http://127.0.0.1:8000/api/likes-per-country/

---

### 📊 Stats Site (`http://127.0.0.1:8001`)
- **Dashboard (requires login)**: http://127.0.0.1:8001/stats-homepage/
- **Login**:                      http://127.0.0.1:8001/stats-homepage/ (admin only)
- **Statistics pages**:
  - Vacations per Country  
  - Overdue Vacations (expired in red)  
  - Likes Statistics (total + per country)  
- **Logout**:                     http://127.0.0.1:8001/logout/  

---

Quick Start (Docker)
--------------------
1. Ensure these files exist in project root:
   - `.env`
   - `docker-compose.yml`
   - `Dockerfile` (main web)
   - `requirements.txt`
   - `data.json` (fixture for countries/vacations)
   - `media/` folder (with uploaded images, e.g. `media/about/banner.jpg`)
   - `stats_site/` (separate Django project for stats)

2. Start everything:
   ```sh
   docker compose up -d --build

Check services:
---------------
docker compose ps
docker compose logs -f web
docker compose logs -f stats

On first run:

DB is migrated and superuser is created automatically.

data.json is loaded if DB is empty.

Media files (images, banners) are served from ./media.

Common Commands

Start (detached): docker compose up -d --build

Stop all: docker compose down

Stop & remove volumes (reset): docker compose down -v

Logs: docker compose logs -f web

Enter main Django container: docker compose exec web bash

Enter stats container: docker compose exec stats bash

Notes

Media files are served from http://127.0.0.1:8000/media/ (e.g. banner images).

Navbar now includes an About link.

Logout now redirects to the login page, not Django’s admin logout template.

Both web and stats wait for Postgres to be ready before starting.


what else:
👉 We need to copy (push) all project images to Docker Hub so you can pull and run them easily elsewhere.