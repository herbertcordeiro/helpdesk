from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from .views import handler404,handler500
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('home.urls')),
    path('adm/', include('adminstrador.urls')),
    path('tickets/', include('ticket.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
    path('', include('recoverypw.urls')),
]

handler404 = handler404
handler500 = handler500


"""pra testar o email python -m smtpd -n -c DebuggingServer localhost:1025"""