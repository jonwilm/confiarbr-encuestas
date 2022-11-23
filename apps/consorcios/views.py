from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Consorcio, Sector


class Consorcios(ListView):
    model = Consorcio
    template_name = "consorcios.html"

    def get_context_data(self, **kwargs):
        consorcios = super().get_context_data(**kwargs)
        context = {
            'consorcios': consorcios['object_list'],
        }
        return context


class Sectores(DetailView):
    model = Consorcio
    template_name = "sectores.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consorcio = self.get_object()
        sectores = Sector.objects.filter(consorcio=consorcio.pk)
        context = {
            'consorcio': consorcio,
            'sectores': sectores,
        }
        return context
