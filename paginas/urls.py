from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('<int:pets_id>', views.ver_pet, name='ver_pet'),
]