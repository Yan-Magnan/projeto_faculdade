from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('<int:pets_id>', views.ver_pet, name='ver_pet'),


    # path('buscar/', views.buscar, name='buscar'),
    # path('profile/', views.profile, name='profile'),
    #
    # path('lista_desejo/', views.lista_desejo, name='lista_desejo'),
    # path('minha_colecao/', views.minha_colecao, name='minha_colecao'),

]