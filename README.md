# Vacation Management System

A full-stack vacation booking and statistics platform with Django backends, React frontend, and PostgreSQL database.

## Quick Start

1. **Start all services:**
```bash
docker compose up -d --build
```

2. **Access the applications:**
- **Main App:** http://localhost:8000 - Vacation booking system
- **React Dashboard:** http://localhost:5173 - Statistics and analytics
- **Django Admin:** http://localhost:8000/admin - Admin interface

## Admin Credentials

- **Username:** `root`
- **Password:** `admin`
- **Email:** `root@email.com`

# user
- **Username:** `amos`
- **Password:** `1234`
*Note: A user 'amos' is also available for testing regular user features.*

## Website Links

| Service | URL | Description |
|---------|-----|-------------|
| Main Vacation Site | http://localhost:8000 | Book vacations, browse destinations |
| Admin Panel | http://localhost:8000/admin | Manage users, vacations, countries |
| Stats Dashboard | http://localhost:5173 | Interactive charts and analytics |
| Stats API | http://localhost:8001 | REST API for statistics |

## API Endpoints

**Main App (Port 8000):**
- `GET /api/vacations/` - All vacations
- `GET /api/countries/` - All countries
- Authentication endpoints for user management

**Stats Backend (Port 8001):**
- `GET /whoami` - Current user info
- `GET /vacations-per-country` - Country statistics
- `GET /vacations-overdue` - Overdue vacations
- `GET /top-likes` - Most liked destinations

## Tests

**Backend Tests (Django):**
```bash
# Test main application
docker compose exec web python manage.py test

# Test stats backend
docker compose exec stats_backend python manage.py test

# Verbose output
docker compose exec web python manage.py test --verbosity=2
```

**Frontend Tests (React):**
```bash
# Run all tests
docker compose exec frontend npm test

# Run tests once (non-watch mode)
docker compose exec frontend npm test -- --run

# Run tests with UI
docker compose exec frontend npm run test:ui
```

## Features

- **User Authentication** - Register, login, session management
- **Vacation Booking** - Browse and book vacation packages
- **Like System** - Rate your favorite destinations
- **Admin Management** - Full CRUD operations via Django admin
- **Statistics Dashboard** - Visual analytics with charts
- **REST APIs** - Full API access for all data

## Technology Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** React, TypeScript, Vite
- **Database:** PostgreSQL
- **Deployment:** Docker Compose
- **Charts:** Recharts

## Development

The system automatically runs migrations and loads sample data on startup. All services are containerized and share the same PostgreSQL database.