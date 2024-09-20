from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField() 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, related_name='comentarios', on_delete=models.CASCADE)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comentario de {self.autor} en {self.publicacion}'

# Create your models here.
