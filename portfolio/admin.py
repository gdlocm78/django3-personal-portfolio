from django.contrib import admin
from .models import Project  #Importa de models de la app portfolio la clase Project

#Aqui se le indica que se quiere ver este modelo dentro de la pagina de administracion de Django
#en este caso el definido en la clase Project
admin.site.register(Project)
