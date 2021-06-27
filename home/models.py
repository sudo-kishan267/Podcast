from django.db import models

# Create your models here.
class uploads(models.Model) :
     name = models.CharField(max_length=100)
     pname = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     podcast=models.FileField(default="static\podcasts\1.mp3")
     date = models.DateField() 

     def __str__(self) :
          return self.name
