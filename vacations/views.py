from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Country, Vacation
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import CustomUserCreationForm
from django.db import models
from django.contrib.auth.models import User
from .models import VacationBooking
from .utils import get_country_weather


@login_required
def home(request):
    if not request.user.is_authenticated:
        return render(request, "vacations/landing.html")  # Landing for guests

    countries = Country.objects.all()
    countries_with_weather = []

    for country in countries:
        weather = get_country_weather(country.name)
        countries_with_weather.append((country, weather))

    return render(request, "vacations/home.html", {
        'countries_with_weather': countries_with_weather
    })


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_superuser = False
            user.save()
            messages.success(
                request, "Account created successfully. You can now log in.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "vacations/register.html", {"form": form})


@login_required
def country_detail(request, country_name):
    country = get_object_or_404(Country, name__iexact=country_name)
    vacation_options = country.vacations.all()
    return render(request, 'vacations/country_detail.html', {
        'country_name': country.name,
        'vacation_options': vacation_options
    })


# def home(request):
#    return render(request, "vacations/home.html")

class VacationUpdateView(UserPassesTestMixin, UpdateView):
    model = Vacation
    fields = ['title', 'description', 'image']
    template_name = 'vacations/vacation_form.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        # Check if all required fields are filled
        cleaned_data = form.cleaned_data
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        image = cleaned_data.get('image')

        if title and description and image:
            messages.success(self.request, "Vacation updated successfully ✅")
            return super().form_valid(form)
        else:
            messages.error(
                self.request, "All fields (title, description, image) are required ❌")
            return redirect(self.request.path)

    def form_invalid(self, form):
        messages.error(
            self.request, "Form is invalid. Please check your inputs ❌")
        return self.render_to_response(self.get_context_data(form=form))


@login_required
def choose_vacation(request, vacation_id):
    vacation = get_object_or_404(Vacation, id=vacation_id)
    existing_booking = VacationBooking.objects.filter(
        user=request.user, vacation=vacation).first()

    if request.method == "POST":
        if "delete_booking" in request.POST:
            if existing_booking:
                existing_booking.delete()
                messages.success(request, "Vacation booking cancelled.")
            return redirect("home")

        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        room_type = request.POST.get("room_type")

        if existing_booking:
            existing_booking.start_date = start_date
            existing_booking.end_date = end_date
            existing_booking.room_type = room_type
            existing_booking.save()
            messages.success(request, "Vacation updated successfully.")
        else:
            VacationBooking.objects.create(
                user=request.user,
                vacation=vacation,
                start_date=start_date,
                end_date=end_date,
                room_type=room_type
            )
            messages.success(request, "Vacation booked successfully.")

        return redirect("home")

    return render(request, 'vacations/choose_vacation.html', {
        'vacation': vacation,
        'existing_booking': existing_booking
    })


@login_required
def my_vacations(request):
    bookings = VacationBooking.objects.filter(
        user=request.user).select_related('vacation')

    if request.method == "POST":
        booking_id = request.POST.get("delete_booking_id")
        if booking_id:
            VacationBooking.objects.filter(
                id=booking_id, user=request.user).delete()

    return render(request, 'vacations/my_vacations.html', {
        'bookings': bookings
    })
