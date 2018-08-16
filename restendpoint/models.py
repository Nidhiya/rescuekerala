from django.db import models

# Create your models here.
class Pickup(models.Model):
    name = models.CharField(max_length=50)
    mobilenumber = models.IntegerField()
    address = models.CharField(max_length=100)
    latt = models.IntegerField()
    longitude = models.IntegerField()
    medicalemergency = models.BooleanField(default=False)
    medicalreason = models.TextField()
    no_people = models.IntegerField()

    def __str__(self):
        return(self.name)
