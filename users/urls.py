from django.urls import path
from .views import register, list_users, delete, add_photo
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', list_users, name="users"),
    path('register/', register, name='newUser'),
    path('edit/', add_photo, name='edit'),
]