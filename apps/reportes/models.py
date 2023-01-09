from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from smart_selects.db_fields import ChainedForeignKey

from django.contrib.auth.models import User
from apps.consorcios.models import Consorcio, Sector
from apps.cuestionario.models import Pregunta


class Reporte(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    nombre = models.CharField(
        'Reporte', max_length=255
    )
    consorcio = models.ForeignKey(
        Consorcio, on_delete=models.CASCADE, verbose_name='consorcio'
    )
    sector = models.ForeignKey(
        Sector, on_delete=models.CASCADE, verbose_name='sector'
    )
    slug = models.SlugField(
        'Slug', max_length=255, blank=True, null=True
    )
    estado = models.BooleanField(
        'Finalizado', default=False
    )
    archivo = models.FileField(
        'Archivo de reporte', upload_to='media/reportes', blank=True, null=True
    )
    creacion = models.DateField(
        'Fecha del reporte', auto_now_add=True
    )
    actualizacion = models.DateField(
        'Fecha de Actualización', auto_now=True
    )

    class Meta:

        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'

    def save(self, *args, **kwargs):
        self.nombre = str(self.consorcio) + ' - ' + str(self.sector) + ' - ' + str(self.creacion)
        super(Reporte, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.consorcio) + '-' + slugify(self.sector) + '-' + slugify(self.creacion)
            self.save()

    def __str__(self):
        return str(self.nombre)


RESPUESTA_CHOICES = [
    ('SI', 'SI'),
    ('NO', 'NO')
]


class Respuesta(models.Model):

    reporte = models.ForeignKey(
        Reporte, on_delete=models.CASCADE, verbose_name='reporte'
    )
    pregunta = models.ForeignKey(
        Pregunta, on_delete=models.CASCADE, verbose_name='pregunta'
    )
    respuesta = models.CharField(
        'Respuesta', max_length=2, choices=RESPUESTA_CHOICES, default=None
    )
    observaciones = models.TextField(
        'Observaciones', blank=True, null=True
    )
    imagen1 = models.ImageField(
        'Imagen 1', upload_to='media/img-respuesta', blank=True, null=True
    )
    imagen2 = models.ImageField(
        'Imagen 2', upload_to='media/img-respuesta', blank=True, null=True
    )
    imagen3 = models.ImageField(
        'Imagen 3', upload_to='media/img-respuesta', blank=True, null=True
    )
    imagen4 = models.ImageField(
        'Imagen 4', upload_to='media/img-respuesta', blank=True, null=True
    )

    class Meta:

        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

    def __str__(self):
        return str(self.pregunta.cuestionario)


class Unidad(models.Model):

    reporte = models.ForeignKey(
        Reporte, on_delete=models.CASCADE, verbose_name='reporte'
    )
    unidad = models.CharField(
        'Unidad', max_length=255
    )
    observaciones = models.TextField(
        'Observaciones', blank=True, null=True
    )
    imagen1 = models.ImageField(
        'Imagen 1', upload_to='media/img-unidad', blank=True, null=True
    )
    imagen2 = models.ImageField(
        'Imagen 2', upload_to='media/img-unidad', blank=True, null=True
    )
    imagen3 = models.ImageField(
        'Imagen 3', upload_to='media/img-unidad', blank=True, null=True
    )
    imagen4 = models.ImageField(
        'Imagen 4', upload_to='media/img-unidad', blank=True, null=True
    )

    class Meta:

        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'

    def __str__(self):
        return str(self.reporte.nombre)


class Obras(models.Model):

    reporte = models.ForeignKey(
        Reporte, on_delete=models.CASCADE, verbose_name='reporte'
    )
    obra = models.CharField(
        'Obra en sector común', max_length=255
    )
    observaciones = models.TextField(
        'Observaciones', blank=True, null=True
    )
    imagen1 = models.ImageField(
        'Imagen 1', upload_to='media/img-obra', blank=True, null=True
    )
    imagen2 = models.ImageField(
        'Imagen 2', upload_to='media/img-obra', blank=True, null=True
    )
    imagen3 = models.ImageField(
        'Imagen 3', upload_to='media/img-obra', blank=True, null=True
    )
    imagen4 = models.ImageField(
        'Imagen 4', upload_to='media/img-obra', blank=True, null=True
    )

    class Meta:

        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'

    def __str__(self):
        return str(self.reporte.nombre)


class ImagenRespuesta(models.Model):

    respuesta = models.ForeignKey(
        Respuesta, on_delete=models.CASCADE, verbose_name='respuesta'
    )
    imagen = models.ImageField(
        'Imagen', upload_to='media/img-respuesta', blank=True, null=True
    )

    class Meta:

        verbose_name = 'Imagen Respuesta'
        verbose_name_plural = 'Imagenes respuestas'

    def __str__(self):
        return self.imagen
