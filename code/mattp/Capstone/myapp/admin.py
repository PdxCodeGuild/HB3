from django.contrib import admin

# Register your models here.



from .models import SpeciesData, FishSpeciesModel, ZipcodeModel


class SpeciesDataAdmin(admin.ModelAdmin):
    list_display = ('zip_code', 'species_list')


admin.site.register(SpeciesData, SpeciesDataAdmin)
admin.site.register(FishSpeciesModel)
admin.site.register(ZipcodeModel)