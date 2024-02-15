from django.db import models

# Create your models here.
class Comments(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    def __str__(self):
        return f'{self.user}@{self.post}'
