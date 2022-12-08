from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.consorcios.models import Consorcio, Sector


class ConsorcioResource(resources.ModelResource):

    class Meta:
        model = Consorcio


class ConsorcioAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('nombre', 'slug')
    exclude = ('slug',)
    search_fields = ('nombre',)
    ordering = ('nombre',)


class SectorResource(resources.ModelResource):

    class Meta:
        model = Sector


class SectorAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('consorcio', 'nombre', 'slug',)
    exclude = ('slug',)
    search_fields = ('consorcio', 'nombre',)
    list_filter = ('consorcio',)
    ordering = ('consorcio',)


admin.site.register(Consorcio, ConsorcioAdmin)
admin.site.register(Sector, SectorAdmin)
