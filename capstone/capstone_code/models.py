from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.


# class Profile(models.Model):
#     user = models.ForeignKey(User)
#     address = models.CharField(max_length=30)
#     dob = models.CharField(max_length=25)
#     username = models.ForeignKey(User)
#     password = models.ForeignKey(User)

STOCK_WINERIES = (
    ('SYNCLINE', 'Syncline'),
    ('COR_CELLARS', 'Cor Cellars'),
    ('SLEIGHT_OF_HAND', 'Sleight of Hand'),
    ('MARCHESI','Marchsesi'),
    ('MEMALOOSE',"Memaloose"),
    ('EARTH', 'Earth')
    )





class Winery(models.Model):
    winery_name = models.CharField(max_length=30, unique=True, choices=STOCK_WINERIES)
    winery_addr = models.CharField(max_length=50, help_text='Optional')
    winery_phn = models.IntegerField()

    def __str__(self):
        return self.winery_name

    def __repr__(self):
        return 'winery_name={!r} is located at winery_addr={!r}'. format(self.winery_name, self.winery_addr)



class Wine(models.Model):
    wine_name = models.CharField(max_length=30)
    winery_name = models.CharField(max_length=30, unique=True, choices=STOCK_WINERIES)
    varietal = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    quantity = models.IntegerField()
    #barcode = models.PositiveIntegerField
    #notes = models.CharField(max_length=250)


    def __str__(self):
        return self.wine_name

class Cellar(models.Model):
    wine_name = models.ForeignKey('Wine')
    winery_name = models.ForeignKey('Winery')
    barcode = models.PositiveIntegerField
    user = models.ForeignKey(User)

    def __str__(self):
        return self.wine_name, self.username



