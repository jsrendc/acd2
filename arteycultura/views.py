from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives

from django.template.loader import get_template

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def inicio(request):
    return render(request, "inicio.html")


def enviarCorreo(request):
    #correo = EmailMessage("Prueba de correo", "Saludos", to=["jrendon@edu.uag.mx"])
    #correo.send()
    n="Jairo"
    diccionario = {"x":"y","nombre":n}
    
    plantilla = get_template("correo.html")
    body = plantilla.render(diccionario)
    correo = EmailMultiAlternatives(
            "Prueba 2" #subject
            ,"Mensaje de prueba" #body
            ,"jrendon.uag@gmail.com" #sender
            ,["jrendon@edu.uag.mx"] #receiver
            ,["mavelar2001@gmail.com"] #bcc

    )
    correo.attach_alternative(body,"text/html")

    correo.send()
    return HttpResponse("Hola")




def ingresar(request):
    f = AuthenticationForm()
    if request.method == "POST":
        f = AuthenticationForm(data=request.POST)
        if f.is_valid():
            u = request.POST["username"]
            p = request.POST["password"]
            usr = authenticate(username=u,password=p)
            if usr is not None:
                login(request,usr)
                request.session["variableSesion"]= u 
    return render(request,"login.html",{"formulario":f})


def registraUsuario(request):
    f = UserCreationForm()
    if request.method == "POST":
        f = UserCreationForm(data=request.POST)
        if f.is_valid():
            usr = f.save()
            

    f.fields["username"].help_text = None
    f.fields["password1"].help_text = None
    f.fields["password2"].help_text = None
    return render(request,"agregausuario.html",{"formulario":f})

def salir(request):
    logout(request)
    return HttpResponse("Fuera!")