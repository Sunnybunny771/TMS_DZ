from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField('Name', max_length=50)
    text = models.TextField('Text')
    publication_date = models.DateField(auto_now_add=True, null=True)

    
    def __str__(self) -> str:
        return self.title