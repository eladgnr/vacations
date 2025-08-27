from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
import requests
import time


def fetch_json(url, retries=5, delay=2):
    """Try to fetch JSON from a URL with retries."""
    for i in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # raise error if status != 200
            return response.json()
        except Exception as e:
            print(f"Retry {i+1}/{retries} failed for {url}: {e}")
            time.sleep(delay)
    return {}


def staff_only(user):
    return user.is_authenticated and user.is_staff


def staff_required(view_func):
    return login_required(user_passes_test(staff_only)(view_func))


@login_required
def dashboard(request):
    """
    Main statistics dashboard.
    Pulls data from the vacations backend API running in web:8000.
    """
    base_url = "http://web:8000/api"  # Django web service inside docker

    vacations_stats = fetch_json(f"{base_url}/vacations/stats/")
    users_total = fetch_json(f"{base_url}/users/total/")
    likes_total = fetch_json(f"{base_url}/likes/total/")
    # old distribution (can remove later if not needed)
    likes_distribution = fetch_json(f"{base_url}/likes/distribution/")
    vacations_per_country = fetch_json(f"{base_url}/vacations-per-country/")
    # ✅ new likes per country
    likes_per_country = fetch_json(f"{base_url}/likes-per-country/")

    context = {
        "user": request.user,
        "vacations_stats": vacations_stats,
        "users_total": users_total,
        "likes_total": likes_total,
        "likes_distribution": likes_distribution,
        "vacations_per_country": vacations_per_country,
        "likes_per_country": likes_per_country,
    }
    return render(request, "dashboard.html", context)
