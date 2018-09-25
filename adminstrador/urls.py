from django.urls import path
from .views import inicial

urlpatterns = [
    path('inicial/', inicial, name='inicial'),
]