"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include
from django.contrib import admin
from django.urls import path
from docentes.views import agregar_docente, ver_docente, eliminar_docente, modificar_docente, generar_reporte, DocenteViewSet, InstitucionViewSet, MateriaViewSet
from rest_framework import routers
from webapp.views import bienvenida, bienvenida2

router = routers.DefaultRouter()
router.register(r'docentes', DocenteViewSet)
router.register(r'instituciones', InstitucionViewSet)
router.register(r'materias', MateriaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('bienvenido/', bienvenida),
    path('', bienvenida2, name='inicio'),
    path('agregar_docente/', agregar_docente),
    path('ver_docente/<int:id>', ver_docente),
    path('eliminar_docente/<int:id>', eliminar_docente),
    path('modificar_docente/<int:id>', modificar_docente),
    path('generar_reporte/', generar_reporte),
]
urlpatterns += router.urls

