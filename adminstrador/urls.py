from django.urls import path
from .views import inicial, details, pesquisa_id

urlpatterns = [
    path('', inicial, name='inicial'),
    path('details/<int:id>', details, name='details'),
    path('pesquisa/', pesquisa_id, name='pesquisa'),
]