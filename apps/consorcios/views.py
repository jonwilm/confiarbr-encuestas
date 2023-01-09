from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import Consorcio, Sector

from .forms import LoginForm


class Home(TemplateView):
    template_name = "home.html"


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class Consorcios(ListView):
    model = Consorcio
    template_name = "crear/consorcios.html"

    def get_context_data(self, **kwargs):
        consorcios = super().get_context_data(**kwargs)
        context = {
            'consorcios': consorcios['object_list'],
        }
        return context


class Sectores(DetailView):
    model = Consorcio
    template_name = "crear/sectores.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consorcio = self.get_object()
        sectores = Sector.objects.filter(consorcio=consorcio.pk)
        context = {
            'consorcio': consorcio,
            'sectores': sectores,
        }
        return context


class LogoutView(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('consorcios_app:login'))
