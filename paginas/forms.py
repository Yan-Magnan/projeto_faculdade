from django.forms import ModelForm
from .models import Pets


class PetsForm(ModelForm):

    class Meta:
        model = Pets
        fields = [status, tutor, email, telefone, historico_medico]
