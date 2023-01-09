from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "consorcios_app"

urlpatterns = [
    path(
        'accounts/login/',
        views.LoginView.as_view(),
        name='login',
    ),
    path(
        'logout',
        views.LogoutView.as_view(),
        name='logout',
    ),
    path(
        'crear-reporte/consorcios',
        login_required(views.Consorcios.as_view()),
        name='consorcios-list',
    ),
    path(
        'crear-reporte/<slug:slug>',
        login_required(views.Sectores.as_view()),
        name='sectores-list',
    ),
]
