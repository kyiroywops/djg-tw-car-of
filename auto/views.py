from django.shortcuts import render, redirect
from .models import Auto, Ventas, Compradores, Vendedores, Detalles
from django.http import HttpResponse
from .forms import AutoForm, VentasForm

# Create your views here.

def inicio(request):
    return render(request, "paginas/inicio.html")

def comision(request):
    return render(request, "paginas/comision.html")

def autos(request):
    autos = Auto.objects.all()
    return render(request, "autos/index.html", {"autos": autos})

def login(request):
    return render(request, "paginas/login.html")

def signup(request):
    return render(request, "paginas/signup.html")  

def crear(request):
    formulario = AutoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("autos")
    return render(request, "autos/crear.html", {"formulario": formulario})

def crearVendedor(request):
    return render(request, "paginas/crearVendedor.html")

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

def ventas (request):
    return render(request, "ventas/index.html")

def crearVentas (request):
    formulario = VentasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("ventas")
    return render(request, "ventas/crear.html", {"formulario": formulario})

def editarVentas(request, id):
    ventas = Auto.objects.get(id=id)
    formulario = AutoForm(request.POST or None, request.FILES or None, instance=ventas)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("ventas")
    return render(request, "ventas/editar.html", {"formulario": formulario})

def eliminarVentas(request, id):
    ventas = Ventas.objects.get(id=id)
    ventas.delete()
    return redirect("ventas")


