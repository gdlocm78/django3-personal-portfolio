"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views   #Se indica que se importan las vistas que se crearon en views de la app portfolio para poder usarlas en elos URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),  #Cualquier cosa relacionada al url blog lo va forwardear al archivo urls.py que se encuentra en la aplicacion blog y ahi va manejar todo lo que este abajo de ese url
]

#Deiniendo path para manejar las imagenes en la administracion de django
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
