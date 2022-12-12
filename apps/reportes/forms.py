from django import forms
from django.forms import modelformset_factory, inlineformset_factory

from .models import Reporte, Respuesta, Unidad, ImagenRespuesta


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = []


class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = [
            'pregunta',
            'respuesta',
            'observaciones',
            'imagen1',
            'imagen2',
            'imagen3',
            'imagen4',
        ]
        widgets = {
            'pregunta': forms.HiddenInput(
                attrs={
                    'class': 'form-control disabled',
                }
            ),
            'respuesta': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'observaciones': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Observaciones',
                    'rows': '2',
                    'style': 'resize: none;'
                }
            ),
            'imagen1': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'imagen2': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'imagen3': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'imagen4': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


RespuestaFormSet = modelformset_factory(
    Respuesta,
    form=RespuestaForm,
    extra=0,
)


class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = [
            'unidad',
            'observaciones',
            'imagen1',
            'imagen2',
            'imagen3',
            'imagen4',
        ]
        widgets = {
            'unidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Unidad',
                }
            ),
            'observaciones': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Observaciones',
                    'rows': '2',
                    'style': 'resize: none;'
                }
            ),
            'imagen1': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'imagen2': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'imagen3': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'imagen4': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


UnidadFormSet = modelformset_factory(
    Unidad,
    form=UnidadForm,
    extra=1,
)


class ImagenRespuestaForm(forms.ModelForm):
    class Meta:
        model = ImagenRespuesta
        fields = [
            'respuesta',
            'imagen',
        ]
        widgets = {
            'respuesta': forms.HiddenInput(
                attrs={
                    'class': 'form-control disabled',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


ImagenRespuestaFormSet = inlineformset_factory(
    Respuesta,
    ImagenRespuesta,
    form=ImagenRespuestaForm,
    extra=0,
)
