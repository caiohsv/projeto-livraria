from django.db import models

class Livros(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    resumo = models.TextField()
    genero = models.CharField(max_length=50)
    image  = models.FileField(upload_to = 'livrariaapp/', null = True, blank = True)

    def __str__(self):
        return self.nome