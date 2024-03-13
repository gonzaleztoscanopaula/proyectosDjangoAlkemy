from django.shortcuts import render
from .models import Usuario
from django.http import JsonResponse

# Create your views here.
#create
def crear_usuario(request):
    nuevoUsuario = Usuario.objects.create(
        nombre = "Marcos",
        apellido = "Perez",
        edad = 30
    )    
    return render(request,"usuarios.html",{"nuevoUsuario": nuevoUsuario})

#JSON Response
def ejemplo_json_view(request):
    #Crea un diccionario con los datos que quieres devolver en formato JSON
    data={"mensaje":"Hola desde json response!", "numero":42 }
    #Crea una respuesta JSON
    #return JsonResponse(data)
    return render(request,"json.html",{"data": data})


#read

def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request,"allUsers.html",{"usuarios": usuarios})

def filtrar_usuario(request):
    datosFiltrados =   Usuario.objects.filter(edad=25)
    return render(request,"usersFiltrados.html",{"datosFiltrados": datosFiltrados})

#update
def actualizar_usuario(request, id):
    usuarioActualizar = Usuario.objects.get(id=id)
    usuarioActualizar.edad = 25
    usuarioActualizar.save()
    return render(request,"updatedUser.html",{"updatedUser": usuarioActualizar})
