from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    language = models.CharField(max_length=100)
    price= models.CharField(max_length=6)

    def __str__(self):
        return self.name

