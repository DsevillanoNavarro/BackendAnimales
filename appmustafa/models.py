from datetime import date, timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Animal(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    edad = models.PositiveIntegerField(editable=False, null=True, blank=True) 
    situacion = models.TextField(max_length=750)
    imagen = models.ImageField(upload_to='animales/')

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    def __str__(self):
        return self.nombre

    def calcular_edad(self):
        if self.fecha_nacimiento:
            today = date.today()
            return today.year - self.fecha_nacimiento.year - (
                (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
            )
        return None

    def save(self, *args, **kwargs):
        self.edad = self.calcular_edad()  # Calcula la edad antes de guardar
        super().save(*args, **kwargs)


class Noticia(models.Model):
    titulo=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='noticias/') 
    contenido=models.TextField(max_length=1000)
    fecha_publicacion=models.DateField()
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name="comentarios")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comentarios")
    contenido = models.TextField(max_length=1000)
    fecha_hora = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.contenido[:50] 

    def tiempo_transcurrido(self):
        """Calcula el tiempo transcurrido desde que se creó el comentario"""
        delta = timezone.now() - self.fecha_hora 
        seconds = delta.total_seconds()

        if seconds < 60:
            return f"{int(seconds)}s" 
        elif seconds < 3600:
            return f"{int(seconds // 60)}m"  
        elif seconds < 86400:
            return f"{int(seconds // 3600)}h"  
        elif seconds < 2592000:
            return f"{int(seconds // 86400)}d" 
        else:
            return f"{int(seconds // 2592000)}mo" 

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

class Adopcion(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="adopciones")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adopciones")
    fecha_hora = models.DateTimeField(auto_now_add=True) 
    aceptada = models.BooleanField(default=False)
    contenido = models.TextField(max_length=1000)
    class Meta:
        verbose_name = 'Adopcion'
        verbose_name_plural = 'Adopciones'
    def __str__(self):
        return self.animal.nombre