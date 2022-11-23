from django.contrib import admin
from apps.consorcios.models import Consorcio, Sector


class ConsorcioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'slug')
    exclude = ('slug',)
    search_fields = ('nombre',)
    ordering = ('nombre',)


class SectorAdmin(admin.ModelAdmin):

    list_display = ('consorcio', 'nombre', 'slug',)
    exclude = ('slug',)
    search_fields = ('consorcio', 'nombre',)
    list_filter = ('consorcio',)
    ordering = ('consorcio',)


admin.site.register(Consorcio, ConsorcioAdmin)
admin.site.register(Sector, SectorAdmin)
