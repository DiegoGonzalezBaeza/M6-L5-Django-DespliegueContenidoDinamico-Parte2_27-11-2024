from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    duracion = models.PositiveIntegerField(help_text="Duración en horas")

# Lo siguiente es para que el superadmin lo pueda ver: 
    def __str__(self):
        return self.nombre