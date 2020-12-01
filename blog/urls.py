from django.urls import path
from . import views   #Se indica que se importan las vistas que se crearon en views de la app portfolio

app_name = 'blog'  #como buena practica se recomienda colocar la variable app_name igual a nombre de la app

urlpatterns = [
    path('', views.all_blogs, name="all_blogs"),
    path('<int:blog_id>/', views.details, name="details"),  #Cualquier numbero que se ponga despues de blog/ lo va direccionar a la pagina de detail
]
