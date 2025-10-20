from django import forms
from .models import Socio, Actividad, Inscripcion

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ["nombre", "apellido", "dni", "email"]

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ["nombre", "categoria", "profesor", "cupo"]

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ["socio", "actividad"]

# Formulario para buscar (DNI o Nombre de actividad)
class BusquedaForm(forms.Form):
    OPCIONES = [
        ("dni", "Buscar Socio por DNI"),
        ("actividad", "Buscar Actividad por Nombre"),
    ]
    tipo = forms.ChoiceField(choices=OPCIONES, widget=forms.RadioSelect)
    consulta = forms.CharField(label="Ingrese búsqueda", max_length=50)
