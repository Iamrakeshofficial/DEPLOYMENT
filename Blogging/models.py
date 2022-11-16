from django.db import models

# Create your models here.

class Blogger(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message =models.CharField(max_length=200)



class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    
    def __str__(self):
        return self.title