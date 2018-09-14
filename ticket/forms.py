from django.forms import ModelForm
from ticket.models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["nome_completo", "email", "telefone", "categoria", "anexo", "descricao"]