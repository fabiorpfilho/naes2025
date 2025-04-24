from django.db import models

# Create your models here.


class Status(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nome}"
    