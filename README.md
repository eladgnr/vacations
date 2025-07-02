Django Elad Vacation Site Project
---------------------------------

🔹 Step 1: Clone the Project
git clone https://github.com/eladgnr/vacations
cd <project Folder Path>

🔹 Step 2: Create & Activate Virtual Environment
python -m venv venv
.\venv\Scripts\activate  # For Windows
source venv/bin/activate # For Mac

🔹 Step 3: Install Requirements
pip install -r requirements.txt

🔹 Step 4: Start the Server
python manage.py runserver

Open in Browser
Main site: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin

Run Tests
python manage.py test vacations.tests

Test Users
Username	Password	Role
admin	    1234	    Admin
amos	    1234	    Regular User

This project includes a REST API for managing vacations, available at:
http://127.0.0.1:8000/api/vacations/
