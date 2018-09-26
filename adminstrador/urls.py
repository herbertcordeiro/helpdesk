from django.urls import path
from .views import inicial
from .views import dash

urlpatterns = [
    path('inicial/', inicial, name='inicial'),
]