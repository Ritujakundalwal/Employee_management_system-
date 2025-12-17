A Django-based Employee Management System that helps organizations efficiently manage employee records with a clean dashboard, analytics, and secure authentication.
| Technology          | Purpose                  |
| ------------------- | ------------------------ |
| **Python 3.13**     | Backend Language         |
| **Django 5+**       | Web Framework            |
| **HTML5**           | Frontend Structure       |
| **Bootstrap 5**     | Styling & Responsive UI  |
| **Bootstrap Icons** | UI Icons                 |
| **Chart.js**        | Dashboard Charts         |
| **SQLite**          | Database                 |
| **JavaScript**      | Charts & UI interactions |


employee_project/
│
├── employee/                # Main App
│   ├── templates/employee/  # HTML Templates
│   ├── static/              # CSS, JS, Images
│   ├── models.py            # Employee Model
│   ├── views.py             # App Logic
│   ├── urls.py              # App URLs
│
├── employee_project/        # Project Settings
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3               # Database
├── manage.py
├── requirements.txt
└── README.md

create virtual enviornment
python -m venv venv

Install Dependencies
pip install -r requirements.txt

Apply Migrations
python manage.py makemigrations
python manage.py migrate

Create Superuser (Admin)
python manage.py createsuperuser

admin:nadmin
password:nadmin@123

Run the Server
python manage.py runserver



Author
Rituja Kundalwal
 💻 Django | Python | Web Development
