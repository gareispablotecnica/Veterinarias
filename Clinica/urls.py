from django.urls import path
from .views import *


urlpatterns = [
    path('', Home, name='Home'),
    path('Registro/', Registro, name='Registro'),
    path('Mascotas/', VerMascotas, name='VerMascotas'),
    path('Modificacion/<int:ID_Mascota>/', Modificacion, name='Modificacion'),
    path('Eliminar/<int:ID_Mascota>/',EliminarMascota, name='EliminarMascota'),
]
