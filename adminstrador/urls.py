from django.urls import path
from .views import inicial
from .views import pesquisa_id

urlpatterns = [
    path('inicial/', inicial, name='inicial'),
    path('pesquisa/', pesquisa_id, name='pesquisa'),
]