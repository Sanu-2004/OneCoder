from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    phone=models.CharField(max_length=10)
    msg=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title=models.TextField()
    Subtitle=models.TextField()
    content=models.TextField()
    slug=models.SlugField()
    date=models.DateField()
    img=models.ImageField(upload_to='media/')
    views=models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
