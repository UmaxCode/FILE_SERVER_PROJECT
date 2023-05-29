from django.db import models

# Create your models here.

class Document(models.Model):
    
    title = models.CharField(max_length=200)

    description = models.TextField()

    file = models.FileField()

    def __str__(self):
        
        return self.title
    
    
