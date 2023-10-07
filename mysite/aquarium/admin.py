from django.contrib import admin
from .models import Fish, Specie


# Register your models here.


class FishAdmin(admin.ModelAdmin):
    list_display = ['fish_title', 'origin', 'species']
    list_filter = ['origin', 'species', 'fish_title']

    search_fields = ['fish_title']


class SpecieAdmin(admin.ModelAdmin):
    list_display = ['specie_name', 'display_fish']


admin.site.register(Fish, FishAdmin)
admin.site.register(Specie, SpecieAdmin)
