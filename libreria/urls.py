from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarios/crear', views.crear_usuarios, name='crear'),
    path('usuarios/editar', views.editar_usuarios, name='editar') 
]