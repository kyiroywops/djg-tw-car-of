from django.shortcuts import render, redirect
from .models import Auto
from django.http import HttpResponse
from .forms import AutoForm

# Create your views here.

def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def autos(request):
    autos = Auto.objects.all()
    return render(request, "autos/index.html", {"autos": autos})

def crear(request):
    formulario = AutoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("autos")
    return render(request, "autos/crear.html", {"formulario": formulario})

def editar(request, id):
    auto = Auto.objects.get(id=id)
    formulario = AutoForm(request.POST or None, request.FILES or None, instance=auto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("autos")
    return render(request, "autos/editar.html", {"formulario": formulario})

def eliminar(request, id):
    auto = Auto.objects.get(id=id)
    auto.delete()
    return redirect("autos")
