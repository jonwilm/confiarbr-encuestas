from django.db import models


class Consorcio(models.Model):

    nombre = models.CharField(
        'Consorcio', max_length=255)

    class Meta:

        verbose_name = 'Consorcio'
        verbose_name_plural = 'Consorcios'

    def __str__(self):
        return self.nombre


class Sector(models.Model):

    consorcio = models.ForeignKey(
        Consorcio, on_delete=models.CASCADE, verbose_name='consorcio')
    nombre = models.CharField(
        'Sector', max_length=255)

    class Meta:

        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'

    def __str__(self):
        return self.nombre