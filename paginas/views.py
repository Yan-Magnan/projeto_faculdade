from django.shortcuts import render, get_object_or_404
from .models import Pets, Categoria  # Substituído Livros por Pets
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# @login_required(redirect_field_name='login')
def index(request):
    pets = Pets.objects.all()  # Substituído Livros por Pets
    return render(request, 'paginas/index.html', {
        'pets': pets
    })

# @login_required(redirect_field_name='login')
def ver_pet(request, pets_id):
    pet = get_object_or_404(Pets, id=pets_id)  # Substituído Livros por Pets
    return render(request, 'paginas/ver_pet.html', {
        'pet': pet
    })

# @login_required(redirect_field_name='login')
def profile(request):
    return render(request, 'paginas/profile.html')

# @login_required(redirect_field_name='login')
# def ver_pet(request):
#     pets = Pets.objects.all()  # Substituído Livros por Pets
#     return render(request, 'paginas/ver_pet.html', {
#         'pets': pets,
#     })

# @login_required(redirect_field_name='login')
def lista_desejo(request):
    return render(request, 'paginas/lista_desejo.html')

# @login_required(redirect_field_name='login')
def minha_colecao(request):
    return render(request, 'paginas/minha_colecao.html')

# @login_required(redirect_field_name='login')
def buscar(request):
    search = request.GET.get('search')
    pets = Pets.objects.filter(categoria__nome=search)  # Substituído Livros por Pets
    return render(request, 'paginas/buscar.html', {
        'pets': pets,
    })


