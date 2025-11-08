# Lesson 20 - Python Web Frameworks <!-- omit in toc -->

This lesson provides a comprehensive introduction to Python web frameworks, covering both synchronous and asynchronous approaches to building RESTful APIs. You'll learn to build the same user management API using different frameworks and deployment strategies.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. Flask with Development Server](#01-flask-with-development-server)
  - [02. Flask with Gunicorn (Production Deployment)](#02-flask-with-gunicorn-production-deployment)
  - [03. Quart with Uvicorn (Async Framework)](#03-quart-with-uvicorn-async-framework)
  - [04. Quart with Hypercorn (Alternative ASGI Server)](#04-quart-with-hypercorn-alternative-asgi-server)
  - [05. Django REST Framework (Full-Featured Framework)](#05-django-rest-framework-full-featured-framework)
    - [Project Structure](#project-structure)
    - [User Model (`05/users/models.py`)](#user-model-05usersmodelspy)
    - [Serializers (`05/users/serializers.py`)](#serializers-05usersserializerspy)
    - [API Views (`05/users/views.py`)](#api-views-05usersviewspy)
- [How to Run Examples](#how-to-run-examples)
  - [01. Flask Development Server](#01-flask-development-server)
  - [02. Flask with Gunicorn](#02-flask-with-gunicorn)
  - [03. Quart with Uvicorn](#03-quart-with-uvicorn)
  - [04. Quart with Hypercorn](#04-quart-with-hypercorn)
  - [05. Django REST Framework](#05-django-rest-framework)
- [API Testing Examples](#api-testing-examples)
  - [Test Endpoints with curl](#test-endpoints-with-curl)
    - [Get All Users](#get-all-users)
    - [Get Specific User](#get-specific-user)
    - [Add New User](#add-new-user)
  - [Test with Python requests](#test-with-python-requests)
- [Framework Comparison](#framework-comparison)
  - [Flask](#flask)
  - [Quart](#quart)
  - [Django](#django)
- [Deployment Servers Comparison](#deployment-servers-comparison)
  - [Development Servers](#development-servers)
  - [Production WSGI Servers (Synchronous)](#production-wsgi-servers-synchronous)
  - [ASGI Servers (Asynchronous)](#asgi-servers-asynchronous)
- [Advanced Patterns](#advanced-patterns)
  - [API Versioning](#api-versioning)
  - [Middleware and Request Processing](#middleware-and-request-processing)
  - [Error Handling](#error-handling)
  - [Authentication and Authorization](#authentication-and-authorization)
  - [Database Integration](#database-integration)
  - [Async Database Operations (Quart)](#async-database-operations-quart)
- [Best Practices](#best-practices)
  - [1. **API Design**](#1-api-design)
  - [2. **Response Format Consistency**](#2-response-format-consistency)
  - [3. **Input Validation**](#3-input-validation)
  - [4. **Environment Configuration**](#4-environment-configuration)
  - [5. **Logging and Monitoring**](#5-logging-and-monitoring)
- [Practice Suggestions](#practice-suggestions)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Understand different Python web frameworks and their characteristics
- Learn to build RESTful APIs with Flask, Quart, and Django
- Compare synchronous vs asynchronous web frameworks
- Master different deployment strategies (development server, Gunicorn, Uvicorn, Hypercorn)
- Understand when to choose each framework for specific use cases
- Learn API design patterns and best practices
- Implement CRUD operations in web APIs

## Course Content

### 01. Flask with Development Server
**Files:** `01/api.py`, `01/requirements.txt`, `01/run.sh`, `01/README.md`

Learn the basics of Flask, Python's most popular micro web framework:

```python
#!/usr/bin/env python3

from flask import Flask, jsonify, request, render_template_string
from datetime import datetime

app = Flask(__name__)

# Simulated in-memory "database" of users
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

@app.route("/", methods=["GET"])
def home():
    html = """
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>Flask Home</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f9f9f9; }
            h1 { color: #333; }
            .info { margin-top: 20px; }
            code { background: #eee; padding: 3px 6px; }
        </style>
    </head>
    <body>
        <h1>Welcome to the Flask API Server!</h1>
        <p class="info">Current time: {{ time }}</p>
        <p>Available APIs:</p>
        <ul>
            <li><code>GET /api/users</code> - Get all users</li>
            <li><code>GET /api/users/&lt;id&gt;</code> - Get a specific user</li>
            <li><code>POST /api/users</code> - Add a new user</li>
        </ul>
    </body>
    </html>
    """
    return render_template_string(html, time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/api/users", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Missing name or email"}), 400

    new_id = max(u["id"] for u in users) + 1 if users else 1
    new_user = {"id": new_id, "name": data["name"], "email": data["email"]}
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
```

**Key Concepts:**
- Flask application structure and routing
- HTTP methods (GET, POST) handling
- JSON request/response processing
- Error handling and status codes
- In-memory data storage simulation
- HTML template rendering with `render_template_string`
- URL parameters and path variables

### 02. Flask with Gunicorn (Production Deployment)
**Files:** `02/api.py`, `02/requirements.txt`, `02/run.sh`, `02/README.md`

Learn to deploy Flask applications using Gunicorn for production environments:

**Dependencies (`02/requirements.txt`):**
```
flask
gunicorn
```

**Deployment Command:**
```bash
gunicorn -w 4 -b 0.0.0.0:8000 api:app
```

**Key Concepts:**
- Production-ready WSGI server (Gunicorn)
- Multi-worker process management
- Performance optimization for concurrent requests
- Production deployment best practices
- Process-based scaling vs threading

### 03. Quart with Uvicorn (Async Framework)
**Files:** `03/api.py`, `03/requirements.txt`, `03/run.sh`, `03/README.md`

Explore asynchronous web development with Quart and Uvicorn:

```python
#!/usr/bin/env python3

from quart import Quart, jsonify, request, render_template_string
from datetime import datetime

app = Quart(__name__)

# Simulated in-memory "database" of users
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

@app.route("/", methods=["GET"])
async def home():
    html = """
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>Quart Home</title>
        <!-- styles -->
    </head>
    <body>
        <h1>Welcome to the Quart API Server!</h1>
        <p class="info">Current time: {{ time }}</p>
        <!-- API endpoints list -->
    </body>
    </html>
    """
    return await render_template_string(html, time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route("/api/users", methods=["GET"])
async def get_users():
    return jsonify(users)

@app.route("/api/users/<int:user_id>", methods=["GET"])
async def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
```

**Dependencies (`03/requirements.txt`):**
```
quart
uvicorn
```

**Key Concepts:**
- Asynchronous request handling with `async`/`await`
- Quart as Flask-compatible async framework
- Uvicorn as ASGI server
- Non-blocking I/O operations
- Better performance for I/O-bound applications

### 04. Quart with Hypercorn (Alternative ASGI Server)
**Files:** `04/api.py`, `04/requirements.txt`, `04/run.sh`, `04/README.md`

Learn alternative deployment options for async frameworks:

**Dependencies (`04/requirements.txt`):**
```
quart
hypercorn
```

**Deployment Command:**
```bash
hypercorn api:app --host 0.0.0.0 --port 8000
```

**Key Concepts:**
- Hypercorn vs Uvicorn comparison
- HTTP/2 and WebSocket support
- Alternative ASGI server implementations
- Performance characteristics of different servers

### 05. Django REST Framework (Full-Featured Framework)
**Files:** `05/manage.py`, `05/myproject/`, `05/users/`, `05/requirements.txt`, `05/README.md`

Master Django's comprehensive approach to API development:

#### Project Structure
```
05/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── users/
    ├── __init__.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── migrations/
```

#### User Model (`05/users/models.py`)
```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"
```

#### Serializers (`05/users/serializers.py`)
```python
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']
```

#### API Views (`05/users/views.py`)
```python
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from datetime import datetime

def home(request):
    return render(request, 'home.html', {'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**Dependencies (`05/requirements.txt`):**
```
django
djangorestframework
gunicorn
```

**Key Concepts:**
- Django's Model-View-Template (MVT) architecture
- Object-Relational Mapping (ORM) with models
- Serializers for data validation and transformation
- Database migrations and schema management
- Built-in admin interface
- Comprehensive ecosystem and middleware
- Security features (CSRF, authentication, etc.)

## How to Run Examples

### 01. Flask Development Server
```bash
cd lesson-20/01
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=api.py
flask run
# Or use the run script
bash run.sh

# Access at http://localhost:5000
```

### 02. Flask with Gunicorn
```bash
cd lesson-20/02
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
gunicorn -w 4 -b 0.0.0.0:8000 api:app
# Or use the run script
bash run.sh

# Access at http://localhost:8000
```

### 03. Quart with Uvicorn
```bash
cd lesson-20/03
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api:app --host 0.0.0.0 --port 8000
# Or use the run script
bash run.sh

# Access at http://localhost:8000
```

### 04. Quart with Hypercorn
```bash
cd lesson-20/04
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
hypercorn api:app --host 0.0.0.0 --port 8000
# Or use the run script
bash run.sh

# Access at http://localhost:8000
```

### 05. Django REST Framework
```bash
cd lesson-20/05
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Database setup
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Or run with Gunicorn
gunicorn myproject.wsgi:application

# Access at http://localhost:8000
```

## API Testing Examples

### Test Endpoints with curl

#### Get All Users
```bash
curl -X GET http://localhost:8000/api/users
```

#### Get Specific User
```bash
curl -X GET http://localhost:8000/api/users/1
```

#### Add New User
```bash
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Charlie", "email": "charlie@example.com"}'
```

### Test with Python requests
```python
import requests
import json

base_url = "http://localhost:8000"

# Get all users
response = requests.get(f"{base_url}/api/users")
print("All users:", response.json())

# Add new user
new_user = {"name": "David", "email": "david@example.com"}
response = requests.post(
    f"{base_url}/api/users",
    headers={"Content-Type": "application/json"},
    data=json.dumps(new_user)
)
print("New user:", response.json())

# Get specific user
user_id = 1
response = requests.get(f"{base_url}/api/users/{user_id}")
print(f"User {user_id}:", response.json())
```

## Framework Comparison

### Flask
**Pros:**
- Lightweight and minimalist
- Easy to learn and get started
- Flexible and unopinionated
- Large ecosystem of extensions
- Great for microservices

**Cons:**
- Requires manual configuration for complex apps
- No built-in ORM or admin interface
- Synchronous by default

**Best for:** Microservices, APIs, small to medium applications, learning web development

### Quart
**Pros:**
- Flask-compatible syntax
- Native async/await support
- Better performance for I/O-bound tasks
- WebSocket support
- HTTP/2 support

**Cons:**
- Smaller ecosystem compared to Flask
- Async programming complexity
- Less mature than Flask

**Best for:** Real-time applications, WebSocket-heavy apps, high-concurrency APIs

### Django
**Pros:**
- "Batteries included" philosophy
- Powerful ORM and admin interface
- Built-in security features
- Comprehensive documentation
- Large ecosystem and community

**Cons:**
- Steeper learning curve
- Can be overkill for simple projects
- More opinionated structure
- Larger memory footprint

**Best for:** Large applications, rapid prototyping, content management, enterprise applications

## Deployment Servers Comparison

### Development Servers
- **Flask dev server**: Built-in, single-threaded, development only
- **Django dev server**: Built-in, auto-reload, development only

### Production WSGI Servers (Synchronous)
- **Gunicorn**: Popular, battle-tested, multi-worker
- **uWSGI**: Feature-rich, complex configuration
- **Waitress**: Pure Python, Windows compatible

### ASGI Servers (Asynchronous)
- **Uvicorn**: Fast, based on uvloop and httptools
- **Hypercorn**: HTTP/2 support, more features
- **Daphne**: Django channels compatible

## Advanced Patterns

### API Versioning
```python
# URL path versioning
@app.route("/api/v1/users", methods=["GET"])
def get_users_v1():
    return jsonify(users)

@app.route("/api/v2/users", methods=["GET"])
def get_users_v2():
    # Enhanced response format
    return jsonify({
        "users": users,
        "total": len(users),
        "version": "2.0"
    })
```

### Middleware and Request Processing
```python
# Flask middleware example
@app.before_request
def before_request():
    # Log incoming requests
    print(f"Request: {request.method} {request.path}")

@app.after_request
def after_request(response):
    # Add CORS headers
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
```

### Error Handling
```python
# Custom error handlers
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(ValidationError)
def validation_error(error):
    return jsonify({"error": str(error)}), 400
```

### Authentication and Authorization
```python
from functools import wraps

def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route("/api/users", methods=["POST"])
@require_auth
def add_user():
    # Protected endpoint
    pass
```

### Database Integration
```python
# SQLAlchemy with Flask
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

### Async Database Operations (Quart)
```python
import asyncpg

async def get_users_from_db():
    conn = await asyncpg.connect('postgresql://localhost/testdb')
    rows = await conn.fetch('SELECT * FROM users')
    await conn.close()
    return [dict(row) for row in rows]

@app.route("/api/users", methods=["GET"])
async def get_users():
    users = await get_users_from_db()
    return jsonify(users)
```

## Best Practices

### 1. **API Design**
```python
# Use consistent naming conventions
GET    /api/users          # Get all users
GET    /api/users/123      # Get specific user
POST   /api/users          # Create new user
PUT    /api/users/123      # Update entire user
PATCH  /api/users/123      # Partial update
DELETE /api/users/123      # Delete user
```

### 2. **Response Format Consistency**
```python
# Consistent JSON response structure
def success_response(data, message="Success"):
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    })

def error_response(message, status_code=400):
    return jsonify({
        "status": "error",
        "message": message,
        "data": None
    }), status_code
```

### 3. **Input Validation**
```python
# Request validation
def validate_user_data(data):
    errors = []
    if not data.get('name'):
        errors.append("Name is required")
    if not data.get('email'):
        errors.append("Email is required")
    elif '@' not in data['email']:
        errors.append("Invalid email format")
    return errors

@app.route("/api/users", methods=["POST"])
def add_user():
    data = request.get_json()
    errors = validate_user_data(data)
    if errors:
        return error_response(errors, 400)
    # Process valid data
```

### 4. **Environment Configuration**
```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    DEBUG = os.environ.get('FLASK_DEBUG') == 'True'

app.config.from_object(Config)
```

### 5. **Logging and Monitoring**
```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/api/users", methods=["GET"])
def get_users():
    logger.info("Fetching all users")
    try:
        users = fetch_users()
        logger.info(f"Retrieved {len(users)} users")
        return jsonify(users)
    except Exception as e:
        logger.error(f"Error fetching users: {e}")
        return error_response("Internal error", 500)
```

## Practice Suggestions

1. **Extend the User API**: Add PUT and DELETE operations
2. **Add Data Validation**: Implement comprehensive input validation
3. **Database Integration**: Replace in-memory storage with SQLite/PostgreSQL
4. **Authentication System**: Implement JWT-based authentication
5. **API Documentation**: Add Swagger/OpenAPI documentation
6. **Testing Suite**: Write unit and integration tests
7. **Caching Layer**: Implement Redis-based caching
8. **Rate Limiting**: Add request rate limiting
9. **File Upload**: Implement file upload endpoints
10. **Pagination**: Add pagination for large datasets

## Related Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Quart Documentation](https://pgjones.gitlab.io/quart/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Gunicorn Documentation](https://gunicorn.org/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Hypercorn Documentation](https://pgjones.gitlab.io/hypercorn/)
- [RESTful API Design Best Practices](https://restfulapi.net/)
- [HTTP Status Codes](https://httpstatuses.com/)
- [ASGI Specification](https://asgi.readthedocs.io/)
- [WSGI Specification](https://wsgi.readthedocs.io/)