from django.contrib import admin
from .models import Ticket
from .models import Categoria

admin.site.register(Ticket)
admin.site.register(Categoria)
