from django.contrib import admin
import nested_admin

from apps.reportes.models import Reporte, Respuesta, ImagenRespuesta


class ImagenRespuestaAdmin(nested_admin.NestedStackedInline):
    model = ImagenRespuesta
    extra = 0


class RespuestaAdmin(nested_admin.NestedStackedInline):
    model = Respuesta
    extra = 0
    # inlines = (ImagenRespuestaAdmin,)


class ReporteAdmin(nested_admin.NestedModelAdmin):
    list_display = ('creacion', 'consorcio', 'sector',)
    exclude = ('nombre', 'slug',)
    list_filter = ('consorcio',)
    inlines = (RespuestaAdmin,)

    @admin.display(description='Reporte')
    def get_reporte(self, obj):
        return obj.reporte


admin.site.register(Reporte, ReporteAdmin)
