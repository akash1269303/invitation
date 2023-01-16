from django.db import models

# Create your models here.


class Mymodel(models.Model):
    fullname=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    image=models.ImageField(upload_to='image/')

