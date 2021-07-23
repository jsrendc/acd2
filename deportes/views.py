from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .formulario import FormularioArte

# Create your views here.
def inicio(request):
    return HttpResponse("<a href='deportes/add'>Agregar</a>")

def agregar(request):
    f = FormularioArte()
    if request.method =="POST":
        f = FormularioArte(request.POST)
        if f.is_valid():
            f.save()
            return redirect("/")

    return render(request,"deporte.html",{"form":f})
