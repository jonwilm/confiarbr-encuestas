from django.urls import path

from . import views

app_name = "cuestionarios_app"

urlpatterns = [
    path(
        'cuestionario/<slug:slug>',
        views.Cuestionario.as_view(),
        name='cuestionario',
    ),
]
