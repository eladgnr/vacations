Django Elad Vacation Site Project
---------------------------------

🔹 Step 1: Clone the Project
git clone https://github.com/eladgnr/vacations
cd <project Folder Path>

🔹 Step 2: Create & Activate Virtual Environment
python -m venv venv
#if thats doesnt work run - & "C:\Users\ELADG\AppData\Local\Programs\Python\Python313\python.exe" -m venv venv

# if venv already installed, open bash teminal and run
source venv/Scripts/activate # for windows
source venv/bin/activate # For Mac

# if requirments not already installed
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
