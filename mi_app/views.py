from django.shortcuts import render
from django.http import HttpResponse
from mi_app.models import Curso, Estudiantes, Entregable, Profesor
# Create your views here.

def inicio(request):
    cursos = []
    comision = request.GET.get('comision')  # Obtiene la comisión de la URL de la solicitud
    if comision:
        cursos = Curso.objects.filter(comision=comision)  # Filtra los cursos por comisión

    return render(request, 'inicio.html', {'cursos': cursos})

def ver_estudiantes(request):
    estudiantes = Estudiantes.objects.all()
    return render(request, "ver_estudiantes.html", {'estudiantes': estudiantes})

def ver_cursos(request):
    cursos = Curso.objects.all()
    return render(request, "ver_cursos.html", {'cursos': cursos})

def ver_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "ver_profesores.html", {'profesores': profesores})

def ver_entregables(request):
    entregables = Entregable.objects.all()
    return render(request, "ver_entregables.html", {'entregables': entregables})




def crear_curso(request):
    if request.method == "POST":        #cuando aprieto el boton enviar
        curso_nuevo = Curso(nombre=request.POST["nombre"], comision=request.POST["comision"])
        curso_nuevo.save()
        return render(request, "inicio.html")

    return render(request, "crear_curso.html") #muestra por defecto el form vacio



def crear_entrega(request):
    if request.method == "POST":        #cuando aprieto el boton enviar
        entrega_nueva = Entregable(nombre=request.POST["nombre"], fecha_entrega=request.POST["fecha_entrega"], descripcion=request.POST["descripcion"]) 
        entrega_nueva.save()
        return render(request, "inicio.html")

    return render(request, "crear_entrega.html") #muestra por defecto el form vacio



def crear_estudiante(request):
    if request.method == 'POST':
        estudiante = Estudiantes(nombre=request.POST['nombre'], apellido=request.POST['apellido'], edad=request.POST['edad'], email=request.POST['email'])
        estudiante.save()
        return render(request, "inicio.html")

    return render(request, 'crear_estudiante.html')


def crear_profesores(request):
    if request.method == 'POST':
        profesor = Profesor(nombre=request.POST['nombre'], apellido=request.POST['apellido'], edad=request.POST['edad'], email=request.POST['email'])
        profesor.save()
        return render(request, "inicio.html")

    return render(request, 'crear_profesor.html')


def buscar_curso_por_comision(request):

    comision = request.GET.get('comision')  # Obtiene la comisión de la URL de la solicitud
    if comision:
        cursos = Curso.objects.filter(comision=comision)  # Filtra los cursos por comisión
    else:
        cursos = Curso.objects.all()  # Si no se proporciona una comisión, obtiene todos los cursos

    return render(request, 'ver_cursos.html', {'cursos': cursos})