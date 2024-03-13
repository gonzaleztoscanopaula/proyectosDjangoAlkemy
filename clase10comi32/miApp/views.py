from django.shortcuts import render
from .models import Usuario

# Create your views here.
#create
def crear_usuario(request):
    nuevoUsuario = Usuario.objects.create(
        nombre = "Juan",
        apellido = "Perez",
        edad = 30
    )    
    return render(request,"usuarios.html",{"nuevoUsuario": nuevoUsuario})

#read

def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request,"allUsers.html",{"usuarios": usuarios})

def filtrar_usuario(request):
    datosFiltrados =   Usuario.objects.filter(edad=25)
    return render(request,"usersFiltrados.html",{"datosFiltrados": datosFiltrados})
