from django.contrib import admin
from apps.consorcios.models import Consorcio, Sector


class ConsorcioAdmin(admin.ModelAdmin):

    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)


class SectorAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'consorcio',)
    search_fields = ('consorcio', 'nombre',)
    list_filter = ('consorcio',)
    ordering = ('consorcio', 'nombre')


admin.site.register(Consorcio, ConsorcioAdmin)
admin.site.register(Sector, SectorAdmin)
