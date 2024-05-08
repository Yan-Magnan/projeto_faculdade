from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('<int:livros_id>', views.ver_pet, name='ver_pet'),
    # path('buscar/', views.buscar, name='buscar'), # Remove
    # path('profile/', views.profile, name='profile'), # Remove
    # path('ver_livros/', views.ver_livros, name='ver_livros'), # Remove
    # path('lista_desejo/', views.lista_desejo, name='lista_desejo'),
    # path('minha_colecao/', views.minha_colecao, name='minha_colecao'),

]