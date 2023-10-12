from django.db import models


class TituloCafe (models.Model):
    titulo = models.CharField(max_length=100)
    numero= models.IntegerField
    
class SubtituloCafe (models.Model):
    titulo=models.CharField(max_length=50)
    
class TextoCafe (models.Model):
    titulo=models.CharField()
    

def __str__(self):
    return f' {self.titulo}{self.numero}'

# Create your models here.
