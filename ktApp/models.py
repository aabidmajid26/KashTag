from django.db import models

# Create your models here.

class Hut(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    landmark = models.CharField(max_length=40)


    def __str__(self):
        return self.name + ' near ' + self.landmark
class Hotel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    landmark = models.CharField(max_length=40)

    def __str__(self):
        return self.name+' near '+self.landmark

class SkiShop(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    landmark = models.CharField(max_length=40)

    def __str__(self):
        return self.name+' near '+self.landmark

class SkiLender(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
class Instructor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
class PonyWalla(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class PhonePonyWalla(models.Model):
    fid = models.ForeignKey(PonyWalla,on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=10, unique=True)

class PhoneHut(models.Model):
    fid = models.ForeignKey(Hut,on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=10, unique=True)
class PhoneHotel(models.Model):
    fid = models.ForeignKey(Hotel,on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=10, unique=True)
class PhoneSkiShop(models.Model):
    fid = models.ForeignKey(SkiShop,on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=10, unique=True)
class PhoneSkiLender(models.Model):
    fid = models.ForeignKey(SkiLender,on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=10, unique=True)
class PhoneInstructor(models.Model):
    fid = models.ForeignKey(Instructor,on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=10, unique=True)
