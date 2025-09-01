# Vacations Full-Stack Project

A comprehensive vacation management system with Django backend, React frontend, and PostgreSQL database.

## Project Structure

**Backend Services:**
- **Main Web App** (Port 8000) - Django vacation management
- **Stats Backend** (Port 8001) - Django statistics API  
- **Database** - PostgreSQL with shared data

**Frontend:**
- **React Statistics Dashboard** (Port 5173) - Modern UI for analytics

## Technology Stack

- **Backend:** Python, Django, Django REST Framework
- **Frontend:** React, TypeScript, Vite, Bootstrap
- **Database:** PostgreSQL
- **Deployment:** Docker Compose
- **Charts:** Recharts for data visualization

## Quick Start

1. **Prerequisites:**
   - Docker and Docker Compose installed
   - Create `.env` file in project root

2. **Environment Variables (.env):**
```env
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

VITE_STATS_API_URL=http://localhost:8001/api
```

3. **Start All Services:**
```bash
docker compose up --build
```

## Access Points

| Service | URL | Description |
|---------|-----|-------------|
| Main Django App | http://localhost:8000 | Vacation management system |
| Django Admin | http://localhost:8000/admin | Admin interface |
| Stats API | http://localhost:8001/api | Statistics endpoints |
| React Dashboard | http://localhost:5173 | Interactive statistics frontend |

## Default Admin Credentials

- **Username:** root
- **Password:** admin
- **Email:** root@email.com

## Key Features

### Main Application (Port 8000)
- User registration and authentication
- Country and vacation management
- Vacation booking system
- Like/dislike functionality
- Admin panel for content management

### Statistics Dashboard (Port 5173)
- **Login required** for most features
- Interactive charts and visualizations
- Real-time data from shared database
- Available statistics:
  - Vacations per country
  - Overdue vacations tracking
  - Likes distribution
  - Top-rated destinations

### API Endpoints

**Main App APIs:**
- `GET /api/vacations/` - All vacations
- `GET /api/vacations-per-country/` - Country statistics
- `GET /api/vacations-overdue/` - Overdue vacation data
- `GET /api/likes/distribution/` - Likes by destination

**Stats Backend APIs:**
- `GET /api/whoami/` - Current user info
- `GET /api/vacations-per-country/` - Country stats
- `GET /api/vacations-overdue/` - Overdue data
- `GET /api/top-likes/` - Top-rated vacations

## Docker Management

**Common Commands:**
```bash
# Start services
docker compose up --build

# Start in background
docker compose up -d --build

# View logs
docker compose logs -f frontend
docker compose logs -f web
docker compose logs -f stats_backend

# Stop services
docker compose down

# Reset database
docker compose down -v

# Access container shell
docker compose exec web bash
docker compose exec frontend sh
```

## Development Notes

- All services share the same PostgreSQL database
- Media files served from `http://localhost:8000/media/`
- React development server includes hot reloading
- Database migrations run automatically on startup
- Sample data loaded on first run

## File Structure

```
vacation_site/
├── fe_react_src/           # React frontend
│   ├── src/
│   │   ├── pages/          # React pages
│   │   └── components/     # React components
│   └── public/images/      # Static assets
├── stats_backend/          # Django stats API
├── vacations/              # Main Django app
├── config/                 # Django settings
├── media/                  # Uploaded files
├── docker-compose.yml      # Container orchestration
└── .env                    # Environment variables
```

## React Dashboard Features

- **Public Access:** About page, project information
- **Authenticated Access:** Statistics and charts
- **Interactive Charts:** Using Recharts library
- **Responsive Design:** Bootstrap-based UI
- **Real-time Data:** Live connection to Django APIs




## Routing System

Complete React Router setup with client-side navigation. Default route redirects to stats homepage. Includes 404 error handling for invalid URLs. All pages use Link components for smooth navigation without page refreshes. Routes cover statistics dashboard, data visualizations, about page, and catch-all error handling.


Frontend Tests (React)
# Run all tests
docker compose exec frontend npm test

# Run tests with UI
docker compose exec frontend npm run test:ui

# Run tests once (non-watch mode)
docker compose exec frontend npm test -- --run

Run Tests:
# Run all Django tests
docker compose exec web python manage.py test

# Run specific app tests
docker compose exec web python manage.py test vacations

# Run with verbose output
docker compose exec web python manage.py test --verbosity=2

# Run stats backend tests
docker compose exec stats_backend python manage.py test

Test Coverage:

View responses and authentication
API endpoint functionality
Database operations and models
User access control

Test Files Location:
vacations/tests.py
stats_backend/tests.py