from django.contrib import admin
from .models import Categoria, Livros, pet
class LivrosAdmin(admin.ModelAdmin):
    # list_display = ('id', 'nome', 'editora', 'ano_Lancamento', 'categoria', 'mostrar')
    list_display = ('id', 'status', 'nome', 'raca', 'tutor', 'email', 'telefone', 'cpf', 'endereco', 'data_acolhimento', 'historico_medico')
    list_display_links = ('status', 'nome', 'raca', 'tutor', 'email', 'telefone', 'cpf', 'endereco', 'data_acolhimento', 'historico_medico')


list_per_page = 5

admin.site.register(Categoria)
admin.site.register(pet)
admin.site.register(Livros, LivrosAdmin)
# admin.site.register(MeusLivro)


