Django Elad Vacation Site Project
---------------------------------

Project Overview
----------------
This project is a Django web app for managing vacations, users, and countries, with admin and user roles, a REST API, and a statistics dashboard in development.

What’s Implemented
------------------
- Backend: Django project with PostgreSQL DB, models for countries, vacations, bookings, likes, and user authentication.
- REST API: Endpoint for vacations at: 
  http://127.0.0.1:8000/api/vacations/
- Admin Panel: 
  http://127.0.0.1:8000/admin
- Stats API: 
  http://127.0.0.1:8000/api/vacation-stats/ 
  (Returns stats: number of countries, vacations, likes, and users logged in during the last week)
- Test Users:

    Username | Password | Role
    ---------|----------|----------
    admin    | 1234     | Admin
    amos     | 1234     | Regular User

Setup Instructions
------------------

Step 1: Clone the Project
-------------------------
git clone https://github.com/eladgnr/vacations
cd <project Folder Path>

Step 2: Create & Activate Virtual Environment
---------------------------------------------
# Windows (PowerShell):
python -m venv venv
.\venv\Scripts\activate

# If that doesn't work:
& "C:\Users\ELADG\AppData\Local\Programs\Python\Python313\python.exe" -m venv venv

# Mac/Linux:
python3 -m venv venv
source venv/bin/activate

Step 3: Install Requirements
----------------------------
pip install -r requirements.txt

Step 4: Start the Server
------------------------
python manage.py runserver

Open in Browser:
----------------
Main site: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin

Running Tests
-------------
python manage.py test vacations.tests

API Endpoints
-------------
- Vacations API: http://127.0.0.1:8000/api/vacations/
- Statistics API: http://127.0.0.1:8000/api/vacation-stats/

What’s Next / TODO
------------------
- Frontend: Create a React app (in /frontend) to display statistics using the /api/vacation-stats/ endpoint.
- Dashboard: Build a stats dashboard showing number of countries, vacations, likes, and recent user logins.
- (Optional Future Steps):
    - Add charts/graphs to the stats dashboard.
    - Allow time-range filtering for statistics.
    - Add more stats (most liked vacation, top country, etc.).
    - Secure the stats API for admin or staff users only, if needed.

How to Operate the Statistics App
---------------------------------
(Current: Backend only, API returns JSON)

- Start Django as usual (python manage.py runserver)
- Open http://127.0.0.1:8000/api/vacation-stats/ in your browser to see live site stats.

Once the React frontend is added, further instructions will be provided here.
