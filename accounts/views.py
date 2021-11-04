from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        print("usuario ou senha invalidos")
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        print('logado com sucesso ')
        return redirect('index')




def logout(request):
    return render(request, 'accounts/logout.html')



def cadastro(request):
    # if request.method != 'POST':
    return render(request, 'accounts/cadastro.html')
    # #     print('nada postado')
    #
    # email = request.POST.get('email')
    # usuario = request.POST.get('usuario')
    # senha = request.POST.get('senha')
    # senha2 = request.POST.get('senha2')
    #
    # if not usuario or not email or not senha or not senha2:
    #     print('Nenhum campo pode ficar vazio')
    #     return render(request, 'accounts/cadastro.html')
    #
    # try:
    #     validate_email(email)
    #
    # except:
    #     print('Email invalido')
    #     return render(request, 'accounts/cadastro.html')
    #
    # if len(senha) < 6:
    #     print('A senha precisa ter no mínimo 6 caracteres')
    #     return render(request, 'accounts/cadastro.html')
    #
    # if len(usuario) < 3:
    #     print('O usuario precisa ter no mínimo 3 caracteres')
    #     return render(request, 'accounts/cadastro.html')
    #
    # if senha != senha2:
    #     print('As senhas não são iguais')
    #     return render(request, 'accounts/cadastro.html')
    #
    # if User.objects.filter(username=usuario).exists():
    #     print('O usuario já esta cadastrado')
    #     return render(request, 'accounts/cadastro.html')
    #
    # if User.objects.filter(email=email).exists():
    #     print('E-mail já esta cadastrado')
    #     return render(request, 'accounts/cadastro.html')
    #
    #
    # user = User.objects.create_user(username=usuario, email=email, password=senha)
    # user.save()
    # print('Rgistrado com sucesso')
    # return render(request, 'paginas/index.html')





@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
