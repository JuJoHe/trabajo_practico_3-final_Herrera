from django.db import models

class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=12, unique=True)
    email = models.EmailField(blank=True, null=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.dni})"

class Actividad(models.Model):
    nombre = models.CharField(max_length=60)
    categoria = models.CharField(max_length=60, blank=True)
    profesor = models.CharField(max_length=60, blank=True)
    cupo = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre}"

class Inscripcion(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.socio} → {self.actividad}"
