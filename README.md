# React + Django App

A full-stack app built with:
- **Backend:** Django + Django REST Framework
- **Frontend:** React (Vite)
- **API Communication:** Axios
- **CORS:** django-cors-headers

## Setup

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver