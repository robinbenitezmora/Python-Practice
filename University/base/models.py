from django.db import models

class City(models.Model):
    city_code = models.CharField(max_length=7, primary_key=True, unique=True, verbose_name='Code of city')
    city_uf = models.CharField(max_length=2, verbose_name='UF')
    city_name = models.CharField(max_length=50, verbose_name='City')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.city_name

class Country(models.Model):
    code_country = models.CharField(max_length=3, primary_key=True, unique=True, verbose_name='Code of Country')
    country_name = models.CharField(max_length=50, verbose_name='Country')

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country_name
        