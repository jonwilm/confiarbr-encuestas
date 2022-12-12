from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, TemplateView, View

from apps.consorcios.models import Consorcio, Sector
from apps.cuestionario.models import Cuestionario, Pregunta
from .models import Reporte, Respuesta, Unidad, ImagenRespuesta

from .forms import ReporteForm, RespuestaForm, RespuestaFormSet, UnidadFormSet, ImagenRespuestaFormSet

from datetime import date
from django.utils import timezone

# import os
# from django.conf import settings
# from django.template import Context
# from django.template.loader import get_template
# from xhtml2pdf import pisa


class ReporteView(CreateView):
    model = Reporte
    form_class = ReporteForm
    template_name = "crear/reporte.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug_sector = self.kwargs.get('slug')
        sector = Sector.objects.get(slug=slug_sector)
        cuestionario = Cuestionario.objects.get(sector=sector.id)
        preguntas = Pregunta.objects.filter(
            cuestionario=cuestionario.pk,
            estado=True,
            prox_visita__lte=timezone.now()
        )
        context['sector'] = sector
        context['preguntas'] = preguntas
        if "respuesta_formset" not in context:
            context['respuesta_formset'] = RespuestaFormSet(
                queryset=Respuesta.objects.none(),
            )
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        slug_sector = self.kwargs.get('slug')
        sector = Sector.objects.get(slug=slug_sector)
        respuesta_formset = RespuestaFormSet(request.POST, request.FILES)
        if respuesta_formset.is_valid() and form.is_valid():
            return self.form_valid(form, respuesta_formset, sector)
        else:
            return self.form_invalid(form, respuesta_formset)

    def form_invalid(self, form, respuesta_formset):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                respuesta_formset=respuesta_formset,
            )
        )

    def form_valid(self, form, respuesta_formset, sector):
        reporte = form.save(commit=False)
        reporte.consorcio = sector.consorcio
        reporte.sector = sector
        reporte.save()
        instancesResp = respuesta_formset.save(commit=False)
        for instanceResp in instancesResp:
            if instanceResp.respuesta != None:
                instanceResp.reporte = reporte
                instanceResp.save()
                pregunta = Pregunta.objects.get(id=instanceResp.pregunta.id)
                pregunta.ultima_visita = date.today()
                pregunta.save()
        # intancesImg = imagen_respuesta_formset.save(commit=False)
        # for instanceImg in intancesImg:
        #     if instanceImg.imagen != None:
        #         instanceImg.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return str(self.success_url)


class ReporteUnidadView(CreateView):
    model = Reporte
    form_class = ReporteForm
    template_name = "crear/reporte-unidad.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug_sector = self.kwargs.get('slug')
        sector = Sector.objects.get(slug=slug_sector)
        context['sector'] = sector
        if "unidad_formset" not in context:
            context['unidad_formset'] = UnidadFormSet(
                queryset=Unidad.objects.none(),
            )
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        slug_sector = self.kwargs.get('slug')
        sector = Sector.objects.get(slug=slug_sector)
        unidad_formset = UnidadFormSet(request.POST, request.FILES)
        if unidad_formset.is_valid() and form.is_valid():
            return self.form_valid(form, unidad_formset, sector)
        else:
            return self.form_invalid(form, unidad_formset)

    def form_invalid(self, form, unidad_formset):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                unidad_formset=unidad_formset,
            )
        )

    def form_valid(self, form, unidad_formset, sector):
        if Reporte.objects.filter(
            consorcio=sector.consorcio,
            sector=sector,
            creacion=date.today(),
        ).exists():
            getReporte = Reporte.objects.get(
                consorcio=sector.consorcio,
                sector=sector,
                creacion=date.today(),
            )
            reporte = getReporte
        else:
            reporte = form.save(commit=False)
            reporte.consorcio = sector.consorcio
            reporte.sector = sector
            reporte.save()
        instancesUnit = unidad_formset.save(commit=False)
        for instanceUnit in instancesUnit:
            if instanceUnit.unidad != None:
                instanceUnit.reporte = reporte
                instanceUnit.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return str(self.success_url)


class ConsorciosReportes(ListView):
    model = Consorcio
    template_name = "reportes/consorcios.html"

    def get_context_data(self, **kwargs):
        consorcios = super().get_context_data(**kwargs)
        context = {
            'consorcios': consorcios['object_list'],
        }
        return context


class ReportesList(DetailView):
    model = Consorcio
    template_name = "reportes/reporte-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consorcio = self.get_object()
        # reportes = Reporte.objects.filter(consorcio=consorcio.pk)
        reportes = Reporte.objects.filter(consorcio=consorcio.pk).values_list('creacion', flat=True).distinct()
        context = {
            'consorcio': consorcio,
            'reportes': reportes,
        }
        print(context)
        return context


class ReporteSectores(TemplateView):
    template_name = "reportes/sectores-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consorcio = Consorcio.objects.get(slug=kwargs['slug'])
        reportes = Reporte.objects.filter(
            consorcio=consorcio,
            creacion=kwargs['date'],
        )
        context = {
            'consorcio': consorcio,
            'reportes': reportes,
            'fecha': reportes[0].creacion,
        }
        return context
    

class ReporteDetail(DetailView):
    model = Reporte
    template_name = "reportes/reporte.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reporte = self.get_object()
        respuestas = Respuesta.objects.filter(
            reporte=reporte.pk
        )
        unidades = Unidad.objects.filter(
            reporte=reporte.pk
        )
        context = {
            'reporte': reporte,
            'respuestas': respuestas,
            'unidades': unidades,
        }
        print(respuestas)
        return context


class ReporteFull(TemplateView):
    template_name = 'reportes/reporte-full.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consorcio = Consorcio.objects.get(slug=kwargs['slug'])
        reportes = Reporte.objects.filter(
            consorcio=consorcio,
            creacion=kwargs['date'],
        )
        context = {
            'consorcio': consorcio,
            'reportes': reportes,
            'fecha': reportes[0].creacion,
        }
        return context


# class ReporteFull(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('reportes/reporte-full.html')
#         consorcio = Consorcio.objects.get(slug=kwargs['slug'])
#         reportes = Reporte.objects.filter(
#             consorcio=consorcio,
#             creacion=kwargs['date'],
#         )
#         context = {
#             'consorcio': consorcio,
#             'reportes': reportes,
#             'fecha': reportes[0].creacion,
#         }
#         html = template.render(context)
#         response = HttpResponse(content_type='application/pdf')
#         # response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
#         pisaStatus = pisa.CreatePDF(
#             html, dest=response
#         )
#         if pisaStatus.err:
#             return HttpResponse('No se pudo cargar el reporte PDF')

#         return response
