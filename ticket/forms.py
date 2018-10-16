from django import forms
from ticket.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["nome_completo", "email", "telefone", "categoria", "anexo", "descricao"]