from django.db import models

# Create your models here.

class Document(models.Model):
    
    title = models.CharField(max_length=200)

    description = models.TextField()

    file = models.FileField()

    num_downloads = models.PositiveBigIntegerField(default=0)

    num_shares = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        
        return self.title
    
    
