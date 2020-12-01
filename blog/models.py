from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    #Esta funcion hace que los nombres de los objectos en la seccion de administracion de Django se muestren en lugar de que diga object()
    def __str__(self):
        return self.title
