from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .models import Cuestionario, Pregunta, Respuesta
from .forms import RespuestaForm, RespuestaFormSet


class Cuestionario(CreateView):
    model = Cuestionario
    form_class = RespuestaForm
    template_name = "cuestionario.html"
    # success_url = reverse_lazy('consorcios_app:consorcios-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cuestionario = self.get_object()
        preguntas = Pregunta.objects.filter(
            cuestionario=cuestionario.pk
        )
        context['cuestionario'] = cuestionario
        context['preguntas'] = preguntas
        return context

    # def form_valid(self, form, social_formset, paymethod_formset):
    #     service = form.save(commit=False)
    #     service.user = self.request.user
    #     service.save()
    #     instancesSocial = social_formset.save(commit=False)
    #     for instanceSocial in instancesSocial:
    #         instanceSocial.service = service
    #         instanceSocial.save()
    #     instancesPaymethod = paymethod_formset.save(commit=False)
    #     for instancePaymethod in instancesPaymethod:
    #         instancePaymethod.service = service
    #         instancePaymethod.save()
    #     return HttpResponseRedirect(self.get_success_url())

    # def get_success_url(self):
    #     return str(self.success_url)
