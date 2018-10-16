from django import forms
from ticket.models import Ticket
from django.contrib.admin import widgets  

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["data_entrega", "STATUS"]