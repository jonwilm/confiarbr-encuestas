from django.contrib import admin
# import nested_admin

from apps.cuestionario.models import Cuestionario, Pregunta, Respuesta, ImagenRespuesta


class PreguntaAdmin(admin.StackedInline):
    model = Pregunta
    extra = 0


class CuestionarioAdmin(admin.ModelAdmin):
    inlines = (PreguntaAdmin,)
    list_display = ('nombre',)
    exclude = ('nombre',)
    list_filter = ('consorcio',)
    ordering = ('consorcio',)


class ImagenRespuestaAdmin(admin.StackedInline):
    model = ImagenRespuesta
    extra = 0


class RespuestaAdmin(admin.ModelAdmin):
    inlines = (ImagenRespuestaAdmin,)
    list_display = ('pregunta', 'respuesta',)


admin.site.register(Cuestionario, CuestionarioAdmin)
admin.site.register(Respuesta, RespuestaAdmin)


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
