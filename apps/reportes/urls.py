from django.urls import path

from . import views

app_name = "reportes_app"

urlpatterns = [
    path(
        'consorcios/<slug:slug>/crear-reporte/',
        views.ReporteView.as_view(),
        name='reporte',
    ),
]
