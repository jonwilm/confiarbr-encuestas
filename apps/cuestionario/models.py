from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from apps.consorcios.models import Consorcio, Sector


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

    class Meta:

        verbose_name = 'Cuestionario'
        verbose_name_plural = 'Cuestionarios'

    def save(self, *args, **kwargs):
        super(Cuestionario, self).save(*args, **kwargs)
        if not self.nombre:
            self.nombre = str(self.consorcio) + ' - ' + str(self.sector)
            self.save()

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
        'Texto para informe (Prev. Si/No)', max_length=255, help_text='(se puede observar que tal area)'
    )
    text_informe_post = models.CharField(
        'Texto para informe (Post. Si/No', max_length=255, help_text='(se encuentran en buen estado)'
    )
    estado = models.BooleanField(
        'Activa', default=True
    )
    time_prox_visita = models.IntegerField(
        'Proxima Visita en Días', default=1
    )

    class Meta:

        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return self.pregunta


class Reporte(models.Model):

    estado = models.BooleanField(
        'Finalizado', default=False
    )
    archivo = models.FileField(
        'Archivo de reporte', upload_to='media/reportes', blank=True, null=True
    )
    creacion = models.DateTimeField(
        'Fecha de creación', auto_now_add=True
    )
    actualizacion = models.DateTimeField(
        'Fecha de Actualización', auto_now=True
    )


RESPUESTA_CHOICES = [
    ('S', 'SI'),
    ('N', 'NO')
]

class Respuesta(models.Model):

    pregunta = models.ForeignKey(
        Pregunta, on_delete=models.CASCADE, verbose_name='pregunta'
    )
    respuesta = models.CharField(
        'Respuesta', max_length=2, choices=RESPUESTA_CHOICES
    )
    observaciones = models.TextField(
        'Observaciones', blank=True, null=True
    )

    class Meta:

        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

    def __str__(self):
        return str(self.pregunta.cuestionario)


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
