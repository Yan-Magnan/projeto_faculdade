from django.contrib import admin
from .models import Categoria, Livros
class LivrosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'editora', 'ano_Lancamento', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome')
    list_per_page = 5

admin.site.register(Categoria)
admin.site.register(Livros, LivrosAdmin)
# admin.site.register(MeusLivro)


