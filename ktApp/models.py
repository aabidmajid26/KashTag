from django.db import models

# Create your models here.

#Services

class Hut(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    landmark = models.CharField(max_length=40)
    available = models.BooleanField(default=True)
    rating = models.CharField(max_length=1, null=True)


    def __str__(self):
        return self.name + ' near ' + self.landmark

    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'landmark': self.landmark,
            'available' : self.available,
            'rating' : self.rating
        }



class Hotel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    landmark = models.CharField(max_length=40)
    available = models.BooleanField(default=True)
    rating = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.name+' near '+self.landmark
    
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'landmark': self.landmark,
            'available' : self.available,
            'rating' : self.rating
        }

class SkiShop(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    landmark = models.CharField(max_length=40)

    def __str__(self):
        return self.name+' near '+self.landmark
    
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'landmark': self.landmark,
        }

class SkiLender(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
        }
class Instructor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
        }
class PonyWalla(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
        }

#Phone Numbers

class PhonePonyWalla(models.Model):
    fid = models.ForeignKey(PonyWalla,on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=10, unique=True)
    def serialize(self):
        return {
            'fid' : self.fid,
            'phoneNumber' : self.phone_number
        }

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

class AccomodationHut(models.Model):
    fid = models.ForeignKey(Hut, on_delete=models.PROTECT)
    c_rooms = models.IntegerField()
    c_occupied = models.IntegerField()

class AccomodationHotel(models.Model):
    fid = models.ForeignKey(Hotel, on_delete=models.PROTECT)
    c_rooms = models.IntegerField()
    c_occupied = models.IntegerField()