from django.urls import path

from . import views

app_name = "consorcios_app"

urlpatterns = [
    path(
        'crear-reporte/consorcios',
        views.Consorcios.as_view(),
        name='consorcios-list',
    ),
    path(
        'crear-reporte/<slug:slug>',
        views.Sectores.as_view(),
        name='sectores-list',
    ),
]
