from django.urls import path
from .views import relatorios

urlpatterns = [
    path('', relatorios, name='relatorios'),
]