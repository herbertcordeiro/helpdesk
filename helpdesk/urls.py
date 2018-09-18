from django.contrib import admin
from django.urls import path, include
from .views import index
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home', index, name='home'),
    path('tickets/', include('ticket.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
]
