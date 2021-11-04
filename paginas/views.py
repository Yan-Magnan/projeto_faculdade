from django.shortcuts import render, get_object_or_404
from .models import Livros
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login')
def index(request):
    livros = Livros.objects.all()
    return render(request, 'paginas/index.html', {
        'livros': livros
    })

@login_required(redirect_field_name='login')
def abre_livro(request, livros_id):
    # livro = Livros.objects.get(id=livros_id)
    livro = get_object_or_404(Livros, id=livros_id)
    return render(request, 'paginas/abre_livro.html', {
        'livro': livro
    })

@login_required(redirect_field_name='login')
def profile(request):
    return render(request, 'paginas/profile.html')




@login_required(redirect_field_name='login')
def ver_livros(request):
    # messages.add_message(request, messages.ERROR, 'Ocorreu algum erro')
    livros = Livros.objects.all()
    return render(request, 'paginas/ver_livros.html', {
        'livros': livros
    })


@login_required(redirect_field_name='login')
def lista_desejo(request):
    return render(request, 'paginas/lista_desejo.html')

@login_required(redirect_field_name='login')
def minha_colecao(request):
    return render(request, 'paginas/minha_colecao.html')

