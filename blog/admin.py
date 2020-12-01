from django.contrib import admin
from .models import Blog #Se importa la clase Blog que se encuentra definida en el archivo models.py de la app blog.

#Aqui se le indica que se quiere ver este modelo dentro de la pagina de administracion de Django
#en este caso el definido en la clase Blog
admin.site.register(Blog)
