""""Criação de formulário para atualização dos registros de pets no banco de dados."""

from django.forms import ModelForm
from .models import Pets

"""
Funcionamento:

Para usar esse formulário no site, é necessário importar essa classe de formulário na view desejada, e então chamar essa classe, lembrando que para métodos GET ela é chamada sem argumentos, e que para métodos POST ela é chamada com o argumento request.POST. Além disso, esse formulário permite a criação de novas instâncias (NÃO SEI COMO FUNCIONA PARA ESSE CASO, EM QUE NEM TODOS CAMPOS DO FORMULÁRIO E DO MODELO CORRESPONDEM), para conseguir atualizar um objeto, o formulário deve ser chamado com outro argumento:

- A instância de objeto que será atualizada, a qual deve ser obtida do banco de dados usando o próprio Django, e então passada como argumento nominal, no formato: "instance= <instancia_de_objeto_do_banco_de_dados>"
"""

class PetsForm(ModelForm):
    """Uso do ModelForm, nativo do Django, que gera formulários especificamente para atualização ou criação de instâncias de objetos do banco de dados"""

    class Meta:
        model = Pets
        fields = [status, tutor, email, telefone, historico_medico]
