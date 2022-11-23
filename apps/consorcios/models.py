from django.db import models
from django.utils.text import slugify


class Consorcio(models.Model):

    nombre = models.CharField(
        'Consorcio', max_length=255, unique=True
    )
    slug = models.SlugField(
        'Slug', max_length=255, unique=True
    )

    class Meta:

        verbose_name = 'Consorcio'
        verbose_name_plural = 'Consorcios'

    def save(self, *args, **kwargs):
        super(Consorcio, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.nombre)
            self.save()

    def __str__(self):
        return self.nombre


class Sector(models.Model):

    consorcio = models.ForeignKey(
        Consorcio, on_delete=models.CASCADE, verbose_name='consorcio')
    nombre = models.CharField(
        'Sector', max_length=255
    )
    slug = models.SlugField(
        'Slug', max_length=255, blank=True, null=True
    )

    class Meta:

        unique_together = ['consorcio', 'nombre']
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.consorcio) + '-' + slugify(self.nombre)
        super(Sector, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre