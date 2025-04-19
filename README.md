# 📦 C_61_Yash Dubey Final Assignment

![Flask App](https://img.shields.io/badge/Flask-2.2.5-blue) ![Django App](https://img.shields.io/badge/Django-4.2-green) ![Docker](https://img.shields.io/badge/Docker-Compose-blue) ![Python](https://img.shields.io/badge/Python-3.10-yellow)

A consolidated repository containing:

- 🚀 **Part 1: Flask Application**
- 📚 **Part 2: Django Application**
- 🐳 **Part 3: Docker Compose Setup**

All components are containerized and can be run together with Docker Compose.

---

## 🔍 Project Structure
```
C_61_Yash Dubey_Final_Assignment/
├── flask_app/                # Flask application
│   ├── app.py                # Main application
│   ├── requirements.txt      # Python dependencies
│   ├── templates/            # Jinja2 HTML templates
│   └── static/style.css      # Stylesheet
├── django_app/               # Django application
│   ├── manage.py
│   ├── requirements.txt
│   ├── project/              # Django project config
│   └── items/                # "items" app (models, views, templates)
├── Dockerfile.flask          # Flask Dockerfile
├── Dockerfile.django         # Django Dockerfile
└── docker-compose.yml        # Compose file to orchestrate services
```

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose installed
- Git (to clone this repo)
- Internet connection (for pulling base images)

### 1. Clone the Repo
```bash
git clone https://github.com/<your-username>/C_61_Yash_Dubey_Final_Assignment.git
cd C_61_Yash_Dubey_Final_Assignment
```

### 2. Build & Run Containers
```bash
docker-compose up --build
```
- **Flask App**: http://localhost:5000
- **Django App**: http://localhost:8000

> Containers will rebuild automatically on first run.

### 3. Rerun After Changes
```bash
docker-compose up --build
# or rebuild a single service:
docker-compose up --build flask
docker-compose up --build django
# to run in detached mode:
docker-compose down && docker-compose up -d --build
```

---

## ✅ Verification

1. **Flask**
   - Visit `/` to see **Hello, World!**
   - Visit `/greet` to test form validation and greeting

2. **Django**
   - Visit `/` to view and add items
   - Create superuser and test `/admin/` to manage items

3. **Docker**
   - `docker-compose ps` to list services
   - `docker images` to verify built images
   - `docker logs -f flask` / `docker logs -f django` for real-time logs

---

## 📦 Pushing to Docker Hub
```bash
docker login
# Tag locally built images
docker tag flask:latest yashdubey2004/flask_app:latest
docker tag django:latest yashdubey2004/django_app:latest
# Push to your Hub
docker push yashdubey2004/flask_app:latest
docker push yashdubey2004/django_app:latest
```

> Update `docker-compose.yml` to use `image:` instead of `build:` for production deployments.

---

---

*Happy Coding!* 🎉

