from django.db import models

class Persona(models.Model):
    nombre= models.CharField(max_length=18)
    apellido= models.CharField(max_length=18)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"nombre:{self.nombre}, apellido:{self.apellido}, Fecha Nacimiento{self.fecha_nacimiento}"

