from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('socios/alta/', views.socio_alta, name='socio_alta'),
    path('actividades/alta/', views.actividad_alta, name='actividad_alta'),
    path('inscripciones/alta/', views.inscripcion_alta, name='inscripcion_alta'),
    path('buscar/', views.buscar, name='buscar'),
]
