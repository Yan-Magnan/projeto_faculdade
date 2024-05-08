from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Pets


def index(request):
    pets = Pets.objects.all()
    return render(request, 'paginas/index.html', {
        'livros': pets
    })


def abre_livro(request, livros_id):
    # livro = Livros.objects.get(id=livros_id)
    pet = get_object_or_404(Pets, id=livros_id)
    superuser = request.user.is_superuser
    return render(request, 'paginas/abre_livro.html', {
        'livro': pet,
        'superuser': superuser,
    })


@login_required(redirect_field_name='login')
def profile(request):
    return render(request, 'paginas/profile.html')


@login_required(redirect_field_name='login')
def ver_livros(request):
    # messages.add_message(request, messages.ERROR, 'Ocorreu algum erro')

    pets = Pets.objects.all()
    return render(request, 'paginas/ver_livros.html', {
        'livros': pets,
    })

    # categoria = Categoria.objects.all()
    # return render(request, 'paginas/ver_livros.html', {
    #     'categoria': categoria,
    # })


def buscar(request):
    search = request.GET.get('search')
    print(search)

    if search:
        pets = Pets.objects.filter(nome__icontains=search)
    else:
        pets = Pets.objects.all()

    return render(request, 'paginas/buscar.html', {
        'livros': pets,
    })
