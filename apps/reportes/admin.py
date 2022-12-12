from django.contrib import admin
import nested_admin

from apps.reportes.models import Reporte, Respuesta, Unidad, ImagenRespuesta


class ImagenRespuestaAdmin(nested_admin.NestedStackedInline):
    model = ImagenRespuesta
    extra = 0


class RespuestaAdmin(nested_admin.NestedStackedInline):
    model = Respuesta
    extra = 0
    # inlines = (ImagenRespuestaAdmin,)


class UnidadAdmin(nested_admin.NestedStackedInline):
    model = Unidad
    extra = 0


class ReporteAdmin(nested_admin.NestedModelAdmin):
    list_display = ('creacion', 'consorcio', 'sector',)
    exclude = ('nombre', 'slug',)
    list_filter = ('consorcio',)
    inlines = (RespuestaAdmin, UnidadAdmin)

    @admin.display(description='Reporte')
    def get_reporte(self, obj):
        return obj.reporte


admin.site.register(Reporte, ReporteAdmin)
