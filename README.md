# django-auth-core

A production-ready Django authentication backend implementing secure user signup, login, logout, and session-based authentication using Django’s built-in auth system.

---

## 🚀 Features

* User Signup with validation
* Secure Login & Logout
* Password hashing (Django default – PBKDF2 + salt)
* Session-based authentication
* Protected routes using `login_required`
* Django Admin panel integration
* Clean app-based project structure

---

## 🛠️ Tech Stack

* **Backend:** Django
* **Database:** SQLite (default, easily switchable)
* **Auth:** Django built-in authentication system
* **Language:** Python

---

## 📂 Project Structure

```
django-auth-core/
├── core/          # Project configuration
├── accounts/      # Authentication app (signup, login, logout)
├── manage.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/django-auth-core.git
cd django-auth-core
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows
```

3. Install dependencies:

```bash
pip install django
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

---

## 🌐 Available Routes

* `/accounts/signup/` – User registration
* `/accounts/login/` – User login
* `/accounts/logout/` – User logout
* `/accounts/dashboard/` – Protected user dashboard
* `/admin/` – Django admin panel

---

## 🔐 Security Notes

* Passwords are never stored in plain text
* CSRF protection enabled by default
* Authentication handled using Django’s trusted mechanisms

---


