from django.contrib import admin
from .models import Country, Vacation, VacationBooking


@admin.register(VacationBooking)
class VacationBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'vacation', 'start_date', 'end_date', 'room_type')
    list_filter = ('room_type', 'start_date', 'end_date', 'vacation__country')
    search_fields = ('user__username', 'vacation__title')


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Country, CountryAdmin)
admin.site.register(Vacation)
