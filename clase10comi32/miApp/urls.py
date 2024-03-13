from django.urls import path
from. import views

urlpatterns = [
    path("", views.crear_usuario),
    path("all", views.mostrar_usuarios),
    path("filter", views.filtrar_usuario)
    ]