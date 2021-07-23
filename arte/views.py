from typing import Generic
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from .formulario import FormularioArte
from .models import Arte

# Create your views here.

def inicio(request):
    
    #return HttpResponse("<a href='arte/add'>Agregar</a>")
    return render(request,"arte.html")
    


def agregar(request):
    f = FormularioArte()
    if request.method =="POST":
        f = FormularioArte(request.POST)
        if f.is_valid():
            f.save()
            return redirect("/")

    return render(request,"arte.html",{"form":f})


#=====================================
class ListaActividades(generic.ListView):
    model = Arte
    context_object_name = "actividadesarte"
    template_name = "arte.html"