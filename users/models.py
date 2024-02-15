from django.db import models

# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length=50)
    username = models.CharField(max_length=25)
    descr = models.CharField(max_length=150)
    email = models.EmailField()
    since = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='fotos_perfil/', blank=True)
    def __str__(self):
        return f'{self.username} : ({self.id})'
