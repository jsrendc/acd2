from django.shortcuts import redirect, render
from registro.formulario import FormularioPersona

# Create your views here.
def registro(request):
    formulario =  FormularioPersona()
    if request.method == "POST":
        formulario=FormularioPersona(request.POST)
        if formulario.is_valid():
            formulario.save()
            nombre= request.POST["nombre"]
            #print(nombre)
            return redirect("/")
    return render(request,"registro.html", {"form":formulario})
