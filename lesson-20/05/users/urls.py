from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/users', views.get_users, name='get_users'),
    path('api/users/<int:user_id>', views.get_user, name='get_user'),
    path('api/users', views.add_user, name='add_user_post'),
]
