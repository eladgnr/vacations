# 🌴 Django Elad Vacation Site Project

A vacation browsing & booking app built with Django and PostgreSQL.

---

## 🚀 Getting Started

### 1. Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 2. Configure the PostgreSQL database

In `settings.py`, the default DB config is:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vacations_db',
        'USER': 'admin',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Make sure PostgreSQL is running, and the database `vacations_db` exists with a user `admin` (password `1234`).

---

### 3. Run migrations

```bash
python manage.py migrate
```

---

### 4. Start the server

```bash
python manage.py runserver
```

Then visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Sample Users

- **Admin user**  
  `username: admin`  
  `password: 1234`

- **Regular user**  
  `username: amos`  
  `password: 1234`

---

## Run Tests

```bash
python manage.py test
```

---

## Notes

- Images and uploads are stored in the `media/` folder.
- Do **not** upload your `venv/` (virtual environment) folder when sharing the project.
