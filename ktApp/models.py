from django.db import models

# Create your models here.

class Hut(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    landmark = models.CharField(max_length=40)


    def __str__(self):
        return self.name + ' near ' + self.landmark

