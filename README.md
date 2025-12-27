# Task Dependency Tracker

A full-stack Task Dependency Management System built using **Django** (backend) and **React** (frontend).

## Features
- Create tasks with status tracking
- Add dependencies between tasks
- Detect and prevent circular dependencies
- Automatically update task status based on dependencies
- Visualize task dependency graph
- REST API backend with React UI

---

## Tech Stack
- Backend: Django, Django REST Framework
- Frontend: React (hooks)
- Database: SQLite (can be replaced with MySQL)
- Visualization: SVG / Canvas

---

## Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
