from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from .views import handler404,handler500
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('', include('adminstrador.urls')),
    path('tickets/', include('ticket.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
    path('', include('recoverypw.urls')),
    path('ajustes',include('ajustes.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = handler404
handler500 = handler500


"""pra testar o email python -m smtpd -n -c DebuggingServer localhost:1025"""