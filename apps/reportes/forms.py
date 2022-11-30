from django import forms
from django.forms import modelformset_factory

from .models import Reporte, Respuesta


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
        }


RespuestaFormSet = modelformset_factory(
    Respuesta,
    form=RespuestaForm,
    extra=0,
)
