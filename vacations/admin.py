from django.contrib import admin
from .models import Country, Vacation


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Country, CountryAdmin)
admin.site.register(Vacation)
