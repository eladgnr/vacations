Django Elad Vacation Site Project

1. Clone the Project
```bash
git clone https://github.com/eladgnr/vacations
cd <project-folder>  # insert the path you want the project
2. Install Python Dependencies

pip install -r requirements.txt
3. Install PostgreSQL and Set Up the Database
If you want to connect to PostgreSQL manually, use:

psql -U admin -d vacations_db
Then run the following SQL commands (via pgAdmin or psql):


CREATE DATABASE vacations_db;
CREATE USER admin WITH PASSWORD '1234';
GRANT ALL PRIVILEGES ON DATABASE vacations_db TO admin;
These must match the credentials in your settings.py.

4. Run Migrations

python manage.py migrate
5. Create Sample Users
a. Run the Django shell:


python manage.py shell
b. Then paste this:


from django.contrib.auth.models import User
User.objects.create_superuser(username='admin', email='admin@example.com', password='1234')
User.objects.create_user(username='amos', email='amos@example.com', password='1234')
exit()
6. Run the Server

python manage.py runserver
Then visit: http://127.0.0.1:8000/

Sample Users
Username	Password	Role
admin	1234	Superuser
amos	1234	Regular user

If You Want to Run Tests

python manage.py test