from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from vacations.models import Country, Vacation, VacationLike
from django.contrib.auth.models import User  # If you use Django's default User


def stats_summary(request):
    num_countries = Country.objects.count()
    num_vacations = Vacation.objects.count()
    num_likes = VacationLike.objects.filter(is_like=True).count()

    # Users logged in during the last 7 days
    one_week_ago = timezone.now() - timedelta(days=7)
    num_recent_users = User.objects.filter(
        last_login__gte=one_week_ago).count()

    # (Optional: Add more stats if needed)

    return JsonResponse({
        'countries': num_countries,
        'vacations': num_vacations,
        'likes': num_likes,
        'recent_users': num_recent_users,
        # Add more stats here if you want!
    })
