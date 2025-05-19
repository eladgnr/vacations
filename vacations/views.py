from django.shortcuts import render, get_object_or_404
from .models import Country


def country_detail(request, country_name):
    country = get_object_or_404(Country, name__iexact=country_name)
    vacation_options = country.vacations.all()  # via related_name='vacations'

    return render(request, 'vacations/country_detail.html', {
        'country_name': country.name,
        'vacation_options': vacation_options
    })


def home(request):
    countries = Country.objects.all()
    return render(request, 'vacations/home.html', {'countries': countries})
