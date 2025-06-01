#  Library Management System

A full-featured digital library management web application built with Django. It supports user authentication, book browsing, adding to cart, save-for-later, issuing books, and admin panel controls. Designed with a clean UI and deployable on PythonAnywhere.

---

##  Features

- 🔐 User Registration & Login
- 📖 Browse Books with Filters (Author, Most Issued, etc.)
- 🛒 Add to Cart and Save for Later
- 📚 Book Rent Price and ISBN View
- 🖼 Book Cover Image Upload
- 📊 Admin Panel for Managing Books and Users
- ⚙️ Django REST API Integration
- 🎨 Custom UI with background images and logos
- 🌐 Deployed on PythonAnywhere

---

## 🛠️ Tech Stack

- **Backend:** Django 5.0.1, Django REST Framework
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (Default), switchable to PostgreSQL
- **Hosting:** [PythonAnywhere](https://www.pythonanywhere.com/)

---

## 🧩 Installation & Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/vilgax62/library_management_system.git
   cd library_management_system

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt
or
download manually:
pip install django
pip install djangorestframework
pip install djoser
pip install djangorestframework-simplejwt
pip install pillow  # For image uploads
 
4.Requirement version:
Python 3.11
django>=5.0
djangorestframework>=3.15
djoser
djangorestframework-simplejwt
pillow

5.If using PostgreSQL:
pip install psycopg2-binary
 

6.Run migrations:
python manage.py makemigrations
python manage.py migrate

7.Create a superuser:
python manage.py createsuperuser


8.Collect static files:
python manage.py collectstatic

9.Run the server:
python manage.py runserver

10. Project Structure
library_management_system/
│
├── home/                    # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── serializers.py
│
├── library_management_system/
│   ├── templates/           # Contains all HTML templates
│   ├── static/              # Contains CSS, JS, and images
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/                   # Uploaded book images
├── manage.py
└── requirements.txt

11. PythonAnywhere Deployment

    a.Upload project to your PythonAnywhere account.

    b.Configure the WSGI file to point to library_management_system.wsgi.

    c.Set static file mappings in the Web > Static Files section:

    /static/ → /home/Vilgax62/library_management_system/
   

    d.Run collectstatic and reload the app.




Author :Vilgax

