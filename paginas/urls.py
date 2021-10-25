from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('profile/', views.profile, name='profile'),
    path('ver_livros/', views.ver_livros, name='ver_livros'),
    path('lista_desejo/', views.lista_desejo, name='lista_desejo'),
    path('minha_colecao/', views.minha_colecao, name='minha_colecao'),

]