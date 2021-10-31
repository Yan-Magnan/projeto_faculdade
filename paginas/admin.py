from django.contrib import admin
from .models import Categoria, Livros

class LivrosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'editora', 'ano_Lancamento', 'categoria')
    list_display_links = ('id', 'nome')
    list_per_page = 2

admin.site.register(Categoria)
admin.site.register(Livros, LivrosAdmin)