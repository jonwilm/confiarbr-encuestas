from django.contrib import admin
# import nested_admin

from apps.cuestionario.models import Cuestionario, Pregunta, Respuesta, ImagenRespuesta, Reporte


class PreguntaAdmin(admin.StackedInline):
    model = Pregunta
    extra = 0


class CuestionarioAdmin(admin.ModelAdmin):
    inlines = (PreguntaAdmin,)
    list_display = ('nombre', 'slug',)
    exclude = ('nombre', 'slug',)
    list_filter = ('consorcio',)
    ordering = ('consorcio',)


class ImagenRespuestaAdmin(admin.StackedInline):
    model = ImagenRespuesta
    extra = 0


class RespuestaAdmin(admin.ModelAdmin):
    inlines = (ImagenRespuestaAdmin,)
    list_display = ('get_cuestionario', 'pregunta', 'respuesta',)

    @admin.display(description='Cuestionario')
    def get_cuestionario(self, obj):
        return obj.pregunta.cuestionario


class ReporteAdmin(admin.ModelAdmin):
    list_display = ('creacion', 'id', 'consorcio', 'sector',)

    @admin.display(description='Reporte')
    def get_reporte(self, obj):
        return obj.reporte


admin.site.register(Cuestionario, CuestionarioAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Reporte, ReporteAdmin)


# class ImagenRespuestaAdmin(nested_admin.NestedStackedInline):
#     model = ImagenRespuesta
#     extra = 0


# class RespuestaAdmin(nested_admin.NestedStackedInline):
#     model = Respuesta
#     extra = 1
#     inlines = (ImagenRespuestaAdmin,)


# class PreguntaAdmin(nested_admin.NestedStackedInline):
#     model = Pregunta
#     extra = 1
#     inlines = (RespuestaAdmin,)


# class CuestionarioAdmin(nested_admin.NestedModelAdmin):
#     inlines = (PreguntaAdmin,)
#     list_display = ('consorcio', 'sector',)
#     list_filter = ('consorcio',)
#     ordering = ('consorcio',)


# admin.site.register(Cuestionario, CuestionarioAdmin)
