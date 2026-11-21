from django.db import models

class Programa(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)
    facultad = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"