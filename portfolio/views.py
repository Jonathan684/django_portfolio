from django.shortcuts import render
from .models import Project

# retorna un diccionario con todos los proyectos creados en admin
def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})



