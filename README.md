# TaskFlow

TaskFlow is a **Flask-based task management web application** designed to help users create, manage, search, filter, and track their tasks through a clean and responsive interface.

The project also includes an **Admin Panel** for managing users, roles, and account status. It demonstrates practical implementation of authentication, authorization, database relationships, CRUD operations, pagination, search, filtering, CSRF protection, migrations, and secure configuration.

---

## 🚀 Features

### User Authentication

* User registration and login
* Secure password hashing
* Logout functionality
* Session-based authentication
* Active/inactive account protection
* Role-based access control

### Task Management

* Create tasks
* Edit tasks
* Delete tasks
* Task status management
* Task priority management
* Due-date support
* User-specific task ownership

### Search & Filtering

* Search tasks by title
* Filter tasks by status
* Users can only access their own tasks

### Admin Panel

* Admin dashboard
* View registered users
* Search users
* Pagination
* Edit user information
* Change user roles
* Activate/deactivate users
* Delete users
* Admin self-protection

### Security & Error Handling

* Password hashing with Werkzeug
* CSRF protection with Flask-WTF
* Protected routes
* User ownership checks
* Role-based authorization
* Custom 404 error page
* Custom 500 error page
* Secret key stored through environment variables

---

## 🛠️ Tech Stack

**Backend**

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-WTF

**Database**

* SQLite
* SQLAlchemy
* Alembic migrations

**Frontend**

* HTML5
* CSS3
* Jinja2 Templates

**Security**

* Werkzeug password hashing
* Flask-WTF CSRF protection
* Environment variables with `python-dotenv`

**Version Control**

* Git
* GitHub

---

## 📁 Project Structure


TaskFlow/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── migrations/
│   ├── versions/
│   └── ...
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── tasks.py
│
├── routes/
│   ├── auth.py
│   ├── user.py
│   ├── admin.py
│   └── task.py
│
├── templates/
│   ├── auth/
│   ├── admin/
│   ├── tasks/
│   ├── user/
│   ├── home.html
│   ├── 404.html
│   └── 500.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│
└── ...


---

## ⚙️ Installation & Setup

### 1. Clone the Repository


git clone https://github.com/ayzakhan28/TaskFlow.git
cd TaskFlow


### 2. Create a Virtual Environment


python -m venv venv


### 3. Activate the Virtual Environment

**Windows PowerShell:**


.\venv\Scripts\Activate.ps1


If PowerShell blocks activation, you can use:


Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


Then activate the environment again:


.\venv\Scripts\Activate.ps1

### 4. Install Dependencies


pip install -r requirements.txt


### 5. Configure Environment Variables

Create a `.env` file in the project root:


SECRET_KEY=your-secret-key


The `.env` file should **not** be committed to GitHub.

---

## 🗄️ Database Setup

TaskFlow uses SQLite with Flask-Migrate.

After installing the dependencies, run:


flask db upgrade


This applies the existing database migrations.

If you are setting up migrations for a new development database, Flask-Migrate can be initialized with:


flask db init


Then migrations can be created and applied with:


flask db migrate -m "Initial migration"
flask db upgrade


---

## ▶️ Run the Application

Start the Flask development server with:


python app.py

The application will be available at:


http://127.0.0.1:5000


Open the address in your browser to use TaskFlow.

---

## 👤 User Roles

TaskFlow supports two user roles:

### User

Regular users can:

* Register and log in
* Create tasks
* Edit their own tasks
* Delete their own tasks
* Search and filter their tasks
* Manage their task status and priorities

### Admin

Administrators can:

* Access the Admin Dashboard
* View users
* Search users
* Edit users
* Change user roles
* Activate/deactivate accounts
* Delete users
* Manage the application from the Admin Panel

---

## 🔐 Security

TaskFlow implements several security practices:

* Passwords are stored using secure hashing instead of plain text.
* CSRF protection is enabled for forms.
* Authentication-protected routes prevent unauthorized access.
* Role checks protect admin functionality.
* Users cannot edit or delete tasks belonging to other users.
* Admins cannot modify or delete their own account through the Admin Panel.
* Sensitive configuration such as the Flask secret key is stored in environment variables.
* `.env`, the SQLite database, virtual environment, and other local files are excluded through `.gitignore`.

---

## 🧩 Database Models

### User

The `User` model contains information such as:


id
name
email
password
role
created_at
profile_image
is_active


### Task

The `Task` model contains:


id
title
description
status
priority
due_date
user_id
created_at


Each task is associated with its owner through `user_id`.

---

## 🔄 Application Flow


User
 │
 ├── Register
 │
 ├── Login
 │
 ├── User Dashboard
 │      │
 │      ├── Create Task
 │      ├── Edit Task
 │      ├── Delete Task
 │      ├── Search
 │      └── Filter
 │
 └── Admin Login
        │
        └── Admin Dashboard
               │
               ├── Manage Users
               ├── Change Roles
               ├── Activate / Deactivate
               └── Delete Users


---

## 🎯 Portfolio Description

**TaskFlow is a full-stack Flask task management application built with Python, Flask, SQLAlchemy, SQLite, Jinja2, and Flask-WTF. The project demonstrates practical backend development including authentication, role-based authorization, CRUD operations, database migrations, user/task relationships, search, filtering, pagination, CSRF protection, secure password hashing, and admin user management.**

This project was built as a practical portfolio application to demonstrate real-world Flask development and database-driven web application architecture.

---

## 📌 Key Learning Outcomes

Through TaskFlow, the project demonstrates experience with:

* Flask application structure
* Blueprints
* Flask-SQLAlchemy
* SQLAlchemy queries
* Database relationships
* CRUD operations
* Flask-Migrate
* Sessions and authentication
* Role-based authorization
* Jinja2 templates
* Form handling
* CSRF protection
* Pagination
* Search and filtering
* Error handling
* Git and GitHub workflow
* Environment-based configuration

---

## 📄 License

This project is created for learning and portfolio purposes.
