from django.contrib import admin
# import nested_admin

from apps.cuestionario.models import Cuestionario, Pregunta


class PreguntaAdmin(admin.StackedInline):
    model = Pregunta
    extra = 0


class CuestionarioAdmin(admin.ModelAdmin):
    inlines = (PreguntaAdmin,)
    list_display = ('nombre', 'slug',)
    exclude = ('nombre', 'slug',)
    list_filter = ('consorcio',)
    ordering = ('consorcio',)
    

admin.site.register(Cuestionario, CuestionarioAdmin)


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
