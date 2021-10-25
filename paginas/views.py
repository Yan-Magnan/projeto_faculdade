from django.shortcuts import render


def index(request):
    return render(request, 'paginas/index.html')


def menu(request):
    return render(request, 'paginas/menu.html')


def profile(request):
    return render(request, 'paginas/profile.html')


def ver_livros(request):
    return render(request, 'paginas/ver_livros.html')


def lista_desejo(request):
    return render(request, 'paginas/lista_desejo.html')


def minha_colecao(request):
    return render(request, 'paginas/minha_colecao.html')