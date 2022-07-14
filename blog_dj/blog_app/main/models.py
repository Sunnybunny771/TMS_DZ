from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField('Name', max_length=50)
    text = models.TextField('Text')
    publication_date = models.DateField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self) -> str:
        return self.title, self.publication_date



