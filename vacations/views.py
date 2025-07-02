from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import VacationForm
from .models import Vacation
from django.shortcuts import render, redirect
from datetime import date  # ✅ Make sure this is at the top
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from datetime import date
from django.contrib.auth.models import User
from .models import Country, Vacation, VacationLike, VacationBooking
from .forms import CustomUserCreationForm
from .utils import get_country_weather
from .forms import VacationForm


@require_POST
@login_required
def vacation_like(request, vacation_id):
    # Only non-admins can vote
    if hasattr(request.user, 'job_id') and request.user.job_id == 2:
        messages.error(request, "Admins cannot vote.")
        return redirect(request.META.get('HTTP_REFERER', '/'))

    vacation = get_object_or_404(Vacation, id=vacation_id)
    is_like = request.POST.get('is_like') == 'true'

    # Check if user has already voted for this vacation
    existing_vote = VacationLike.objects.filter(
        user=request.user, vacation=vacation).first()

    if existing_vote:
        # Update the existing vote only if it's different
        if existing_vote.is_like != is_like:
            existing_vote.is_like = is_like
            existing_vote.save()
    else:
        # Create a new vote
        VacationLike.objects.create(
            user=request.user, vacation=vacation, is_like=is_like)

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
@require_POST
def order_vacation(request, vacation_id):
    vacation = get_object_or_404(Vacation, id=vacation_id)

    # Prevent duplicate bookings
    if VacationBooking.objects.filter(user=request.user, vacation=vacation).exists():
        messages.info(
            request, f"You already ordered the vacation at {vacation.title}.")
    else:
        VacationBooking.objects.create(
            user=request.user,
            vacation=vacation,
            start_date=None,
            end_date=None,
            room_type=None
        )
        messages.success(
            request, f"Vacation at {vacation.title} has been ordered! 🎉")

    return redirect('country_detail', country_name=vacation.country.name)


@login_required
def delete_vacation(request, vacation_id):
    if not request.user.is_staff:
        return redirect('home')

    vacation = get_object_or_404(Vacation, id=vacation_id)
    vacation.delete()
    return redirect('home')


def home(request):
    countries = Country.objects.all()
    return render(request, "vacations/home.html", {
        'countries': countries
    })


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_superuser = False
            user.save()

            login(request, user)  # <-- this logs the user in immediately

            messages.success(
                request,
                "Registration completed successfully. you are now logged in! 😊"
            )
            # <-- adjust this to your vacations home view name
            return redirect("home")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "vacations/register.html", {"form": form})


# @login_required


@login_required
def country_detail(request, country_name):
    country = get_object_or_404(Country, name__iexact=country_name)
    vacation_options = country.vacations.all()

    for vacation in vacation_options:

        vacation.likes = VacationLike.objects.filter(
            vacation=vacation, is_like=True).count()
        vacation.unlikes = VacationLike.objects.filter(
            vacation=vacation, is_like=False).count()
        user_vote = VacationLike.objects.filter(
            vacation=vacation, user=request.user).first()
        vacation.user_vote = user_vote.is_like if user_vote else None

    return render(request, 'vacations/country_detail.html', {
        'country_name': country.name,
        'vacation_options': vacation_options,
        'today': date.today()  # ✅ This is critical
    })


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


def is_admin(user):
    return user.is_superuser  # You can customize this logic


@login_required
@user_passes_test(is_admin)
def add_vacation(request):
    if request.method == 'POST':
        form = VacationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # or another page like 'country_detail'
    else:
        form = VacationForm()
    return render(request, 'vacations/add_vacation.html', {'form': form})
