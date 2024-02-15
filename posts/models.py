from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) 
    date = models.DateTimeField(auto_now_add=True)
    descr = models.CharField(max_length=100)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    comment_counter = models.IntegerField()
    media = models.ImageField(upload_to='media', blank=True)
    class Meta:
        ordering = ['-date']

        
    def __str__(self):
        return f'({self.id}):{self.title}'
    
