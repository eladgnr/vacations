from django.contrib import admin
from django import forms
from .models import Country, Vacation, VacationBooking
from django.core.exceptions import ValidationError
from datetime import date

# Step 1: Create a custom form to block past dates


class VacationAdminForm(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = '__all__'

    def clean_start_date(self):
        start = self.cleaned_data.get('start_date')
        if start and start < date.today():
            raise ValidationError("Start date cannot be in the past.")
        return start

    def clean_end_date(self):
        end = self.cleaned_data.get('end_date')
        if end and end < date.today():
            raise ValidationError("End date cannot be in the past.")
        return end

# Step 2: Attach the form to the Vacation admin


class VacationAdmin(admin.ModelAdmin):
    form = VacationAdminForm
    list_display = ('title', 'country', 'start_date', 'end_date', 'price')
    search_fields = ('title', 'country__name')

# Step 3: Keep your existing booking admin


@admin.register(VacationBooking)
class VacationBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'vacation', 'start_date', 'end_date', 'room_type')
    list_filter = ('room_type', 'start_date', 'end_date', 'vacation__country')
    search_fields = ('user__username', 'vacation__title')

# Step 4: Register Country and Vacation


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Country, CountryAdmin)
admin.site.register(Vacation, VacationAdmin)  # ✅ Use the custom admin here
