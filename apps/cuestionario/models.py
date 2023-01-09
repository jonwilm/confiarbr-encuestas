from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from smart_selects.db_fields import ChainedForeignKey

from apps.consorcios.models import Consorcio, Sector

import datetime


class Cuestionario(models.Model):

    nombre = models.CharField(
        'Cuestionario', max_length=255
    )
    consorcio = models.ForeignKey(
        Consorcio, on_delete=models.CASCADE, verbose_name='consorcio'
    )
    sector = ChainedForeignKey(
        Sector,
        chained_field="consorcio",
        chained_model_field="consorcio",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE,
        verbose_name='sector'
    )
    slug = models.SlugField(
        'Slug', max_length=255, blank=True, null=True
    )

    class Meta:

        unique_together = ['consorcio', 'sector']
        verbose_name = 'Cuestionario'
        verbose_name_plural = 'Cuestionarios'

    def save(self, *args, **kwargs):
        self.nombre = str(self.consorcio) + ' - ' + str(self.sector)
        self.slug = slugify(self.consorcio) + '-' + slugify(self.sector)
        super(Cuestionario, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Pregunta(models.Model):

    cuestionario = models.ForeignKey(
        Cuestionario, on_delete=models.CASCADE, verbose_name='cuestionario'
    )
    pregunta = models.CharField(
        'Pregunta', max_length=255
    )
    text_informe_prev = models.CharField(
        'Texto para informe (Prev. Si/No)', max_length=255, help_text='(se puede observar que tal area)', blank=True, null=True
    )
    text_informe_post = models.CharField(
        'Texto para informe (Post. Si/No', max_length=255, help_text='(se encuentran en buen estado)', blank=True, null=True
    )
    estado = models.BooleanField(
        'Activa', default=True
    )
    time_prox_visita = models.IntegerField(
        'Proxima Visita en Días', default=1
    )
    ultima_visita = models.DateField(
        'Ultima Visita', blank=True, null=True
    )
    prox_visita = models.DateField(
        'Proxima Visita', blank=True, null=True
    )

    class Meta:

        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def save(self, *args, **kwargs):
        if self.ultima_visita:
            self.prox_visita = self.ultima_visita + datetime.timedelta(days=self.time_prox_visita)
        super(Pregunta, self).save(*args, **kwargs)

    def __str__(self):
        return self.pregunta
