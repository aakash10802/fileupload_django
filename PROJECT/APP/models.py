from django.db import models

# Create your models here.
class Image(models.Model):
    photo=models.ImageField(upload_to='images/')
    sign=models.ImageField(upload_to='images/')
    resume=models.FileField(upload_to='files/', null=True, blank=True)

