from django.shortcuts import render, get_object_or_404
from .models import Pets, Categoria
from django.contrib.auth.decorators import login_required



def index(request):
    pets = Pets.objects.all()

    especie = request.GET.get('especie')
    raca = request.GET.get('raca')
    porte = request.GET.get('porte')
    sex = request.GET.get('sex')

    if especie:
        pets = pets.filter(especie=especie)
    if raca:
        pets = pets.filter(raca=raca)
    if porte:
        pets = pets.filter(porte=porte)
    if sex:
        pets = pets.filter(sex=sex)

    return render(request, 'paginas/index.html', {'pets': pets})



def ver_pet(request, pets_id):
    pet = get_object_or_404(Pets, id=pets_id)
    return render(request, 'paginas/ver_pet.html', {'pet': pet})



def profile(request):
    return render(request, 'paginas/profile.html')



def lista_desejo(request):
    return render(request, 'paginas/lista_desejo.html')



def minha_colecao(request):
    return render(request, 'paginas/minha_colecao.html')
