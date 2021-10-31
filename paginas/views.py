from django.shortcuts import render
from .models import Livros


def index(request):
    livros = Livros.objects.all()
    return render(request, 'paginas/index.html', {
        'livros': livros
    })


def abre_livro(request, livros_id):
    livro = Livros.objects.get(id=livros_id)
    return render(request, 'paginas/abre_livro.html', {
        'livro': livro
    })


# def menu(request):
#     return render(request, 'paginas/profile.html')


def profile(request):
    return render(request, 'paginas/profile.html')


def ver_livros(request):
    return render(request, 'paginas/ver_livros.html')


def lista_desejo(request):
    return render(request, 'paginas/lista_desejo.html')


def minha_colecao(request):
    return render(request, 'paginas/minha_colecao.html')