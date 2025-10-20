

# Register your models here.
from django.contrib import admin
from .models import Socio, Actividad, Inscripcion


class SocioAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "dni", "fecha_inscripcion")
    search_fields = ("apellido", "nombre", "dni")


class ActividadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "profesor", "cupo")
    search_fields = ("nombre", "categoria", "profesor")


class InscripcionAdmin(admin.ModelAdmin):
    list_display = ("socio", "actividad", "fecha_inscripcion")
    search_fields = ("socio__apellido", "actividad__nombre")



admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)