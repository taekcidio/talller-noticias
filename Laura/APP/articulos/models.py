from django.db import models

# Create your models here.
class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    resumen = models.TextField()
    detalle = models.TextField()
    foto = models.ImageField(upload_to='noticias/')
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo