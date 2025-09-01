Django Elad Vacation Project
Project Overview

This is a full-stack Django + React project for managing vacations, users, likes, and countries, with role-based access (admin & user), booking system, and REST API.

It includes:

Vacations site (web – Django) – main app for users/admins

Statistics site (stats_backend – Django) – dashboards and reports

React frontend (frontend) – modern UI for statistics site

Shared PostgreSQL database

All parts run only in Docker using docker-compose.

Stack

Backend: Python, Django, Django REST Framework

Frontend: React (Vite, Bootstrap, Axios, React Router)

Database: PostgreSQL

Orchestration: Docker Compose

Admin Credentials (dev/test)
Username: root
Email:    root@email.com
Password: admin

Environment (.env)

Place this file in project root:

POSTGRES_DB=vacations_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=1234
POSTGRES_HOST=db
POSTGRES_PORT=5432

DJANGO_DEBUG=1
DJANGO_SECRET_KEY=dev-insecure-key-change-me
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DJANGO_SUPERUSER_USERNAME=root
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=root@email.com

# React frontend API endpoint (browser → backend)
VITE_API_URL=http://localhost:8001

Project URLs
🌍 Vacations Site (http://127.0.0.1:8000)

Homepage: /

Admin Panel: /admin/

Login / Register: /accounts/login/ , /register/

Country detail: /country/<country_name>/

Book vacation: /vacation/<id>/choose/

My vacations: /my-vacations/

Like vacation: /vacations/<id>/like/

Add/Edit/Delete vacation: /add-vacation/, /vacation/<id>/edit/

Vacations API

GET /api/vacations/ – list

GET /api/vacations/<id>/ – detail

GET /api/vacations-per-country/

GET /api/likes/total/

GET /api/likes-per-country/

📊 Statistics Site (http://127.0.0.1:8001)

Dashboard (login required): /stats-homepage/

Login: /accounts/login/

Logout: /accounts/logout/

API:

GET /api/whoami/

GET /api/vacations-per-country/

GET /api/vacations-overdue/

⚛ React Frontend (http://127.0.0.1:5173)

/stats-homepage – React version of dashboard

/vacations-per-country – chart view

/vacations-overdue – overdue vacations table

Quick Start (Docker)

Make sure the following exist in project root:

.env

docker-compose.yml

Dockerfile (main Django web)

requirements.txt

data.json (fixture for countries/vacations)

media/ folder (images, banners)

Build and start all containers:

docker compose up --build


Open:

Vacations site → http://127.0.0.1:8000

Statistics API site → http://127.0.0.1:8001

React statistics frontend → http://127.0.0.1:5173

Common Commands

Start detached: docker compose up -d --build

Stop all: docker compose down

Stop & reset DB: docker compose down -v

Logs:

docker compose logs -f web

docker compose logs -f stats_backend

docker compose logs -f frontend

Exec inside container:

docker compose exec web bash

docker compose exec stats_backend bash

Notes

All services share the same Postgres DB.

Media files are served from http://127.0.0.1:8000/media/.

On first run:

DB is migrated

Superuser is created automatically

data.json is loaded if DB is empty

👉 Next step: copy/push all images (web, stats_backend, frontend, db) to Docker Hub so you can run this project elsewhere easily.