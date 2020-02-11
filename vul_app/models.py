from django.db import models


# Create your models here.
class Info(models.Model):
    name = models.TextField()
    gender = models.TextField()