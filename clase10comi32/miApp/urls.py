from django.urls import path
from. import views

urlpatterns = [
    path("", views.crear_usuario),
    path("all", views.mostrar_usuarios),
    path("filter/<int:edad>", views.filtrar_usuario),
    path("update/<int:id>", views.actualizar_usuario),
    path("json",views.ejemplo_json_view)
    ]