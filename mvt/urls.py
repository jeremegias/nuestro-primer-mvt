"""mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from familiares_app.views import (monstrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, 
BorrarFamiliar, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar, FamiliarDetalle, MascotaCrear, 
MascotaActualizar, MascotaBorrar, MascotaList, AutomovilList, AutomovilCrear, AutomovilActualizar, AutomovilBorrar)
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('familiares/', monstrar_familiares),
    path('familiares/buscar', BuscarFamiliar.as_view()),
    path('familiares/alta_familiar', AltaFamiliar.as_view()),
    path('familiares/actualizar_familiar/<int:pk>', ActualizarFamiliar.as_view()),
    path('familiares/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/', FamiliarList.as_view()), 
    path('panel-familia/crear', FamiliarCrear.as_view()), 
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('panel-familia/<int:pk>/detalle/', FamiliarDetalle.as_view()),
    path('panel-mascota/', MascotaList.as_view()),
    path('panel-mascota/alta-mascota', MascotaCrear.as_view()),
    path('panel-mascota/<int:pk>/actualizar-mascota', MascotaActualizar.as_view()),
    path('panel-mascota/<int:pk>/borrar-mascota', MascotaBorrar.as_view()),
    path('panel-automovil/', AutomovilList.as_view()),
    path('panel-automovil/alta-automovil', AutomovilCrear.as_view()),
    path('panel-automovil/<int:pk>/actualizar-automovil', AutomovilActualizar.as_view()),
    path('panel-automovil/<int:pk>/Borrar-automovil', AutomovilBorrar.as_view()),
    
]
 

