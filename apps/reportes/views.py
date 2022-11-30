from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from apps.consorcios.models import Consorcio, Sector
from apps.cuestionario.models import Cuestionario, Pregunta
from .models import Reporte, Respuesta

from .forms import ReporteForm, RespuestaForm, RespuestaFormSet

from datetime import date
from datetime import timedelta
from django.utils import timezone


class ReporteView(CreateView):
    model = Reporte
    form_class = ReporteForm
    template_name = "reporte.html"
    success_url = reverse_lazy('consorcios_app:consorcios-list')

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
        respuesta_formset = RespuestaFormSet(request.POST)
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
        cuestionario = Cuestionario.objects.get(sector=sector.id)
        instancesResp = respuesta_formset.save(commit=False)
        for instanceResp in instancesResp:
            instanceResp.reporte = reporte
            instanceResp.save()
        preguntas = Pregunta.objects.filter(
            cuestionario=cuestionario.pk,
            estado=True
        )
        for pregunta in preguntas:
            pregunta.ultima_visita = date.today()
            pregunta.prox_visita = date.today() + timedelta(days=pregunta.time_prox_visita)
            pregunta.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return str(self.success_url)
