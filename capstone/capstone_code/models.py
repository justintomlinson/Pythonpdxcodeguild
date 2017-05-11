from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator


# Create your models here.


class Winery(models.Model):
    winery_name = models.CharField(max_length=30, unique=True)
    winery_addr = models.CharField(max_length=50, blank=True, help_text='Optional')
    winery_phn = models.CharField(max_length=12, blank=True, help_text='Optional')


    def __str__(self):
        return self.winery_name

    def __repr__(self):
        return 'winery_name={!r} is located at winery_addr={!r}'. format(self.winery_name, self.winery_addr)



class Wine(models.Model):
    wine_name = models.CharField(max_length=30)
    winery_name = models.ForeignKey('Winery', on_delete=models.CASCADE)
    varietal = models.CharField(blank=True, max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=1)
    barcode = models.PositiveIntegerField(blank=True)
    notes = models.TextField(blank=True, max_length=250)


    def __str__(self):
        return self.wine_name



class Cellar(models.Model):
    wine_name = models.ForeignKey('Wine')
    winery_name = models.ForeignKey('Winery')
    user = models.ForeignKey(User)

    def __str__(self):
        return self.wine_name, self.user




