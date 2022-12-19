from django.db import models
from livrariaapp.models import Livros
from django.contrib.auth import get_user_model



class Favoritos2(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)
    livros = models.ManyToManyField(Livros, blank=True)

    def __str__(self):
        return str(self.id)
    


    
