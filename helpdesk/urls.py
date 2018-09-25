from django.contrib import admin
from django.urls import path, include
from .views import index
from django.contrib.auth import views as auth_views
from home import urls as home_urls
from adminstrador import urls as adminstrador_urls


urlpatterns = [
    path('', include(home_urls)),
    path('adm/', include(adminstrador_urls)),
    path('tickets/', include('ticket.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
]