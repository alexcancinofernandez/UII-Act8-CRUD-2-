from django.db import models

class ComentarioYouTube(models.Model):
    id_comentario = models.CharField(max_length=255, unique=True, primary_key=True)
    id_video = models.CharField(max_length=255)
    nombre_usuario = models.CharField(max_length=255)
    texto_del_comentario = models.TextField()
    fecha = models.DateField()
    likes_comentario = models.IntegerField(default=0)

    def __str__(self):
        return f"Comentario de {self.nombre_usuario} en el video {self.id_video}"