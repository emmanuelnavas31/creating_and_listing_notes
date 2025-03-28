from django.db import models


class Notas(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    categoria = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['-created_at']
