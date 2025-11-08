# Django REST API

In this lesson, we will create a simple RESTful API using the Django web framework and Django REST Framework. The API will have endpoints to manage a list of users.

## Creating the Project

To create a new Django project, follow these steps:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
django-admin startproject myproject
cd myproject
python manage.py startapp users
```

## Setting Up the API

1. Add `rest_framework` and `users` to the `INSTALLED_APPS` in `myproject/settings.py`.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'users',
]
```

2. Create a simple user model in `users/models.py`.

```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"
```

3. Create serializers in `users/serializers.py`.

```python
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']
```

4. Create views in `users/views.py`.

```python
from django.shortcuts import render

# Create your views here.
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

5. Set up URLs in `users/urls.py`.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/users', views.get_users, name='get_users'),
    path('api/users/<int:user_id>', views.get_user, name='get_user'),
    path('api/users', views.add_user, name='add_user_post'),
]
```

6. Include the `users` URLs in `myproject/urls.py`.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
]
```

## Running the Server

```bash
python manage.py runserver
```
