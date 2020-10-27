from django.db import models

class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='portfolio/images/')
    description = models.TextField()

def __str__(self): #change admin ting how looks
    return self.title
