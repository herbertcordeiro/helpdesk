from django.urls import path, include
from .views import inicial, details, pesquisa_id


urlpatterns = [
    path('', inicial, name='inicial'),
    path('details/<int:id>', details, name='details'),
    path('pesquisa/', pesquisa_id, name='pesquisa'),
    path('relatorios/', include('relatorios.urls')),
    path('users/', include('users.urls')),
]