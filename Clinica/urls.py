from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Registro/', views.Registro, name='Registro'),
    path('Mascotas/', views.VerMascotas, name='VerMascotas'),
    path('Modificacion/<int:ID_Mascota>/', views.Modificacion, name='Modificacion'),
    path('Eliminar/<int:ID_Mascota>/', views.EliminarMascota, name='EliminarMascota'),
]
