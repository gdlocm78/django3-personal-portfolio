from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)  #blank = True significa que es opcional, el campo puede o no contener datos

    #Esta funcion hace que los nombres de los objectos en la seccion de administracion de Django se muestren en lugar de que diga object()
    def __str__(self):
        return self.title
