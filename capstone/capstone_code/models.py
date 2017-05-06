from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from pygments import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.


# class Profile(models.Model):
#     user = models.ForeignKey(User)
#     address = models.CharField(max_length=30)
#     dob = models.CharField(max_length=25)
#     username = models.ForeignKey(User)
#     password = models.ForeignKey(User)


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
    varietal = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=1)
    #barcode = models.PositiveIntegerField
    #notes = models.CharField(max_length=250)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def __str__(self):
        return self.wine_name

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation 
        """
    lexer = get_lexer_by_name(self.language)
    linenos = self.linenos and 'table' or False
    options = self.title and {'title': self.title} or {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Wine, self).save(*args, **kwargs)


class Cellar(models.Model):
    wine_name = models.ForeignKey('Wine')
    winery_name = models.ForeignKey('Winery')
    barcode = models.PositiveIntegerField
    user = models.ForeignKey(User)

    def __str__(self):
        return self.wine_name, self.user



