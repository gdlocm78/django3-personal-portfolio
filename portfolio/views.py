from django.shortcuts import render
from .models import Project   #Importando la clase Project que se declaro en el modulo models

# Create your views here.
def home(request):
    projects = Project.objects.all()  #Se jala lo que se haya guardado en la base de datos y se mete en la variable projects para poder pasarla al template
    return render(request,'portfolio/home.html',{'projects':projects})
