from django.db import models

# Create your models here.
class Brand(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Fuel(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

class Transmission(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name= 'car_brand')
    fuel_type = models.ForeignKey(Fuel, on_delete=models.CASCADE, related_name='car_fuel')
    transmission_type = models.ForeignKey(Transmission, on_delete=models.CASCADE, related_name='car_transmission')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    descripiton = models.TextField()
    value = models.FloatField()

    def __str__(self):
        return self.model

