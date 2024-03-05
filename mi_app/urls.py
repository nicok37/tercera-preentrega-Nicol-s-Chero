#vistas y urls de mi propia aplicacion las ponemos acá, este urls.py lo creamosd nosotros.
from django.urls import path
from mi_app.views import *


urlpatterns = [
    path("crear_curso/", crear_curso, name="crear curso"),
    path("crear_entrega/", crear_entrega, name="crear entrega"),
    path("crear_estudiantes/", crear_estudiante, name="crear estudiante"),
    path("crear_profesores/", crear_profesores, name="crear profesores"),
    path("ver_estudiantes/", ver_estudiantes, name = "ver estudiantes"),
    path("ver_cursos/", ver_cursos, name = "ver cursos"),
    path("ver_profesores/", ver_profesores, name = "ver profesores"),
    path("ver_entregables/", ver_entregables, name = "ver entregables"),
    path("", inicio, name="home"),
]
