from django.urls import path
from .views import inicial
from .views import details
from .views import pesquisa_id


urlpatterns = [
    path('inicial/', inicial, name='inicial'),
    path('details/<int:id>', details, name='details'),
    path('pesquisa/', pesquisa_id, name='pesquisa'),
]