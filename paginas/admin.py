from django.contrib import admin
from .models import Categoria, Pets

class PetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'nome', 'raca', 'tutor', 'email', 'telefone', 'cpf', 'endereco', 'data_acolhimento', 'historico_medico')
    list_display_links = ('status', 'nome', 'raca', 'tutor', 'email', 'telefone', 'cpf', 'endereco', 'data_acolhimento', 'historico_medico')
    list_per_page = 5

admin.site.register(Categoria)
admin.site.register(Pets, PetsAdmin)
