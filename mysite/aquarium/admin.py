from django.contrib import admin
from .models import Fish, Specie, FishReview, Profilis


# Register your models here.


class FishAdmin(admin.ModelAdmin):
    list_display = ['fish_title', 'origin', 'species']
    list_filter = ['origin', 'species', 'fish_title']

    search_fields = ['fish_title']


class SpecieAdmin(admin.ModelAdmin):
    list_display = ['specie_name', 'display_fishs']


class FishReviewAdmin(admin.ModelAdmin):
    list_display = ('fish', 'date_created', 'reviewer', 'content')


admin.site.register(Fish, FishAdmin)
admin.site.register(Specie, SpecieAdmin)
admin.site.register(FishReview, FishReviewAdmin)
admin.site.register(Profilis)
