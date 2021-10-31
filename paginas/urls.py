from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('<int:livros_id>',views.abre_livro, name='abre_livro'),
    path('profile/', views.profile, name='profile'),
    path('ver_livros/', views.ver_livros, name='ver_livros'),
    path('lista_desejo/', views.lista_desejo, name='lista_desejo'),
    path('minha_colecao/', views.minha_colecao, name='minha_colecao'),

]