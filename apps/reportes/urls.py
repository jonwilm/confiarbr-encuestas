from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "reportes_app"

urlpatterns = [
    path(
        'crear-reporte/<slug:slug>/crear',
        login_required(views.ReporteView.as_view()),
        name='reporte-add',
    ),
    path(
        'crear-reporte/<slug:slug>/unidad',
        login_required(views.ReporteUnidadView.as_view()),
        name='reporte-unidad-add',
    ),
    path(
        'crear-reporte/<slug:slug>/obra',
        login_required(views.ReporteObraView.as_view()),
        name='reporte-obra-add',
    ),
    path(
        'reportes/consorcios',
        views.ConsorciosReportes.as_view(),
        name='reportes-consorcios-list',
    ),
    path(
        'reportes/<slug:slug>/',
        views.ReportesList.as_view(),
        name='reportes-list',
    ),
    path(
        'reportes/<str:slug>/<str:date>/',
        views.ReporteSectores.as_view(),
        name='reporte-sectores',
    ),
    path(
        'reportes/<slug:slug>/reporte',
        views.ReporteDetail.as_view(),
        name='reporte',
    ),
    path(
        'reportes/<str:slug>/<str:date>/reporte',
        views.ReporteFull.as_view(),
        name='reporte-full',
    ),
    # path(
    #     'reportes/<str:slug>/<str:date>/',
    #     views.ReporteDetail.as_view(),
    #     name='reporte',
    # ),
]
