from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import handler404
from .views import handler404,handler500
from django.contrib.auth import views as auth_views
from home import urls as home_urls
from users import urls as users_urls
from relatorios import urls as relatorios_urls
from adminstrador import urls as adminstrador_urls
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm,password_reset_complete


urlpatterns = [
    path('', include(home_urls)),
    path('adm/', include(adminstrador_urls)),
    path('tickets/', include('ticket.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
    path('esqueceu-senha/', password_reset, name='esqueceu-senha'),
    path('login/', password_reset_done, name='password_reset_done'),
    re_path('esqueceu-senha/confirmacao/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', password_reset_confirm, name='password_reset_confirm'),
    path('login/', password_reset_complete, name='password_reset_complete'),
    path('relatorios/', include('relatorios.urls')),
]

handler404 = handler404
handler500 = handler500


"""pra testar o email python -m smtpd -n -c DebuggingServer localhost:1025"""