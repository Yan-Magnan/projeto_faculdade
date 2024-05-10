from django.shortcuts import render, get_object_or_404
from .models import Pets, Categoria
from django.contrib.auth.decorators import login_required


def index(request):
    pets = Pets.objects.all()

    especie = request.GET.get('especie')
    raca = request.GET.get('raca')
    porte = request.GET.get('porte')
    sexo = request.GET.get('sexo')

    print("Filtros aplicados:")
    print("Espécie:", especie)
    print("Raça:", raca)
    print("Porte:", porte)
    print("Sexo:", sexo)

    # Inicializa a query com todos os animais
    filtered_pets = pets

    # Aplica os filtros individualmente
    if especie:
        filtered_pets = filtered_pets.filter(especie=especie)
    if raca:
        filtered_pets = filtered_pets.filter(raca=raca)
    if porte:
        filtered_pets = filtered_pets.filter(porte=porte)
    if sexo:
        filtered_pets = filtered_pets.filter(sexo=sexo)

    print("Número de resultados após aplicação dos filtros:", filtered_pets.count())

    # Retorna a página renderizada com os animais filtrados
    return render(request, 'paginas/index.html', {'pets': filtered_pets})


def ver_pet(request, pets_id):
    pet = get_object_or_404(Pets, id=pets_id)
    return render(request, 'paginas/ver_pet.html', {'pet': pet})


def profile(request):
    return render(request, 'paginas/profile.html')


def lista_desejo(request):
    return render(request, 'paginas/lista_desejo.html')


def minha_colecao(request):
    return render(request, 'paginas/minha_colecao.html')
