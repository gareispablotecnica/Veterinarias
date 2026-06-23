from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import logout

from .forms import FormularioRegistro
from .models import Mascota

def Home(request):
    return render(request, 'Base.html')

def Registro(request):
    data = {'Formulario': FormularioRegistro()}
    if request.method == "POST":
        query = FormularioRegistro(data=request.POST, files=request.FILES)
        if query.is_valid():
            query.save()
            data["Mensaje"] = "Mascota Registrada"
        else:
            data['Mensaje'] = "No se pudo Registrar"
    return render(request, 'Pages/Registro.html', data)

def VerMascotas(request):
    query = Mascota.objects.all()
    data = {'VerMascotas': query}
    return render(request, 'Pages/Mascotas.html', data)

def Modificacion(request, ID_Mascota):
    query = get_object_or_404(Mascota, ID_Mascota=ID_Mascota)
    data = {'Formulario': FormularioRegistro(instance=query)}
    if request.method == "POST":
        query = FormularioRegistro(data=request.POST, instance=query, files=request.FILES)
        if query.is_valid():
            query.save()
            data["Mensaje"] = "Datos Modificados"
        else:
            data['Mensaje'] = "No se pudo Modificar"
    return render(request, 'Pages/Registro.html', data)

def EliminarMascota(request, ID_Mascota):
    query = get_object_or_404(Mascota, ID_Mascota=ID_Mascota)
    query.delete()
    return render(request, 'Pages/Confirmacion.html', {'Mensaje': 'Mascota Eliminada'})
