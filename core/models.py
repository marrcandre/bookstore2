from tkinter import CASCADE
from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):  
        return self.descricao

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros')

    def __str__(self):  
        return self.titulo