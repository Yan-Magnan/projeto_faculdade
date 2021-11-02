from django.shortcuts import render, get_object_or_404
from .models import Livros
from django.contrib import messages


def index(request):
    livros = Livros.objects.all()
    return render(request, 'paginas/index.html', {
        'livros': livros
    })


def abre_livro(request, livros_id):
    # livro = Livros.objects.get(id=livros_id)
    livro = get_object_or_404(Livros, id=livros_id)
    return render(request, 'paginas/abre_livro.html', {
        'livro': livro
    })


def profile(request):
    return render(request, 'paginas/profile.html')



def ver_livros(request):
    # messages.add_message(request, messages.ERROR, 'Ocorreu algum erro')
    livros = Livros.objects.all()
    return render(request, 'paginas/ver_livros.html', {
        'livros': livros
    })



def lista_desejo(request):
    return render(request, 'paginas/lista_desejo.html')


def minha_colecao(request):
    return render(request, 'paginas/minha_colecao.html')

