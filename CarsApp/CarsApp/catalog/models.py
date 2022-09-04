from django.db import models
from datetime import datetime

# Create your models here.


class CarBrand(models.Model):

    BRAND = (
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes'),
        ('Honda', 'Honda'),
        ('Haval', 'Haval'),
        ('Gelly', 'Gelly'),
        ('Cherry', 'Cherry'),
        ('Volkswagen', 'Volkswagen'),
        ('Audi', 'Audi'),
        ('Skoda', 'Skoda'),
    )

    brand = models.CharField(max_length=10, choices=BRAND, unique=True)

    def __str__(self):
        return self.brand


class Engine(models.Model):

    TYPE = (
        ('Atmospheric', 'Atmospheric'),
        ('Turbo', 'Turbo')
    )
    VOLUME = (
        ('1.5', '1.5'),
        ('2.0', '2.0'),
        ('2.5', '2.5'),
        ('3.0', '3.0'),
        ('3.5', '3.5'),
    )
    HORSEPOWER = (
        ('126', '126'),
        ('150', '150'),
        ('220', '220'),
        ('250', '250'),
        ('350', '350'),
    )
    FUEL = (
        ('Petrol', 'Petrol'),
        ('Gass', 'Gass'),
        ('Diesel', 'Diesel'),
    )
    type = models.CharField(max_length=11, choices=TYPE)
    volume = models.CharField(max_length=3, choices=VOLUME)
    horsepower = models.CharField(max_length=3, choices=HORSEPOWER)
    fuel = models.CharField(max_length=6, choices=FUEL, default='Petrol')

    def __str__(self):
        return f'{self.volume}, {self.type}, {self.horsepower}, {self.fuel}'


class CarType(models.Model):

    WHEEL_DRIVE = (
        ('4wd', '4wd'),
        ('2wd', '2wd'),
    )
    TRANSMISSION = (
        ('Mechanical', 'Mechanical'),
        ('Robotic', 'Robotic'),
        ('Auto', 'Auto'),
    )
    TYPE = (
        ('SUV', 'SUV'),
        ('Hatchback', 'Hatchback'),
        ('Crossover', 'Crossover'),
        ('Convertible', 'Convertible'),
        ('Sedan', 'Sedan'),
        ('Sports Car', 'Sports Car'),
        ('Coupe', 'Coupe'),
    )
    wheel_drive = models.CharField(max_length=5, choices=WHEEL_DRIVE)
    transmission = models.CharField(max_length=10, choices=TRANSMISSION)
    type = models.CharField(max_length=11, choices=TYPE)

    def __str__(self):
        return f'{self.type}, {self.transmission}, {self.wheel_drive}'


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE,
                              verbose_name='Бренд')
    type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)
    published = models.DateTimeField(default=datetime.now, blank=True)