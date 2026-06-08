Employee Exit Management System

Overview

Employee Exit Management System built using Flask, PostgreSQL, SQLAlchemy, and Render deployment.

The system manages the complete employee exit workflow involving:

- Employee Exit Form
- Manager Review Form
- PWE Review Form
- Top Management Review
- Final Reports
- MIS Reporting


Tech Stack

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-Migrate
- Gunicorn
- Render


Installation

Clone the repository:

git clone <repository-url>
cd employee-exit-management-system

Create virtual environment:

python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

---

Environment Variables

Create the following environment variable:

DATABASE_URL=your_postgresql_connection_string

Example:

DATABASE_URL=postgresql://username:password@host/database

---

Run Locally

python app.py

Application will run on:

http://127.0.0.1:5000

---

Render Deployment

Build Command:

pip install -r requirements.txt

Start Command:

gunicorn app:app

Environment Variable:

DATABASE_URL=<postgresql_database_url>

---

Database Tables

- User
- EmployeeForm
- ManagerForm
- PWEForm
- FinalReview

---

User Roles

- Employee
- Manager
- PWE
- Top Management

---

Features

- Role Based Login
- Employee Exit Submission
- Manager Review Workflow
- PWE Verification
- Top Management Approval
- Final Reports
- MIS Dashboard
- PostgreSQL Database Storage

