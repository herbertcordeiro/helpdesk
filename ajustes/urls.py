from django.urls import path
from .views import register_categoria


urlpatterns = [
    path('', register_categoria, name="register_categoria"),
]