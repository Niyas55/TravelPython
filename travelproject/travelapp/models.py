from django.db import models

# Create your models here.
class Places(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

def __str__(self):
    return self.name

class Themes(models.Model):
    person=models.CharField(max_length=250)
    pic=models.ImageField(upload_to='pics')
    msg=models.TextField()

def __str__(self):
    return self.person