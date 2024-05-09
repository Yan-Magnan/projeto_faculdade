from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:livros_id>', views.abre_livro, name='abre_livro'),
    path('buscar/', views.buscar, name='buscar'),
    path('profile/', views.profile, name='profile'),
    path('ver_livros/', views.ver_livros, name='ver_livros'),
]
