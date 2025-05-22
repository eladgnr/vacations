from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Country, Vacation
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import CustomUserCreationForm


@login_required
def home(request):
    if not request.user.is_authenticated:
        return render(request, "vacations/landing.html")  # Landing for guests
    countries = Country.objects.all()
    return render(request, "vacations/home.html", {"countries": countries})


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
    return render(request, 'vacations/choose_vacation.html', {'vacation': vacation})
