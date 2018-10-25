from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import handler404
from .views import handler404,handler500
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm,password_reset_complete


urlpatterns = [
    path('home', include('home.urls')),
    path('', include('adminstrador.urls')),
    path('tickets', include('ticket.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
    path('esqueceu-senha/', password_reset, name='esqueceu-senha'),
    path('login/', password_reset_done, name='password_reset_done'),
    re_path('esqueceu-senha/confirmacao/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', password_reset_confirm, name='password_reset_confirm'),
    path('login/', password_reset_complete, name='password_reset_complete'),
    
]

handler404 = handler404
handler500 = handler500


"""pra testar o email python -m smtpd -n -c DebuggingServer localhost:1025"""