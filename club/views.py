

# Create your views here.
from django.shortcuts import render, redirect
from .forms import SocioForm, ActividadForm, InscripcionForm, BusquedaForm
from .models import Socio, Actividad

# Página de inicio
def inicio(request):
    return render(request, "club/index.html")

# Alta de socio
def socio_alta(request):
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = SocioForm()
    return render(request, "club/socio_form.html", {"form": form})

# Alta de actividad
def actividad_alta(request):
    if request.method == "POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = ActividadForm()
    return render(request, "club/actividad_form.html", {"form": form})

# Alta de inscripción
def inscripcion_alta(request):
    if request.method == "POST":
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = InscripcionForm()
    return render(request, "club/inscripcion_form.html", {"form": form})

# Buscador (DNI o Actividad)
def buscar(request):
    resultados = None
    form = BusquedaForm(request.GET or None)

    if form.is_valid():
        tipo = form.cleaned_data["tipo"]
        consulta = form.cleaned_data["consulta"]

        if tipo == "dni":
            resultados = Socio.objects.filter(dni__icontains=consulta)
        else:
            resultados = Actividad.objects.filter(nombre__icontains=consulta)

    return render(request, "club/buscar.html", {"form": form, "resultados": resultados})
