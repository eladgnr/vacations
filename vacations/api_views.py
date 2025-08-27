from rest_framework import viewsets
from .models import Vacation, VacationLike
from .serializers import VacationSerializer
from django.utils.timezone import now
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db.models import Count
from django.db import connection


class VacationViewSet(viewsets.ModelViewSet):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer


# Public endpoints — no @login_required
def vacations_stats(request):
    today = now().date()

    past_vacations = Vacation.objects.filter(end_date__lt=today).count()
    ongoing_vacations = Vacation.objects.filter(
        start_date__lte=today, end_date__gte=today
    ).count()
    future_vacations = Vacation.objects.filter(start_date__gt=today).count()

    data = {
        "pastVacations": past_vacations,
        "ongoingVacations": ongoing_vacations,
        "futureVacations": future_vacations,
    }
    return JsonResponse(data)


def users_total(request):
    total_users = User.objects.count()
    return JsonResponse({"totalUsers": total_users})


def likes_total(request):
    total_likes = VacationLike.objects.filter(is_like=True).count()
    return JsonResponse({"totalLikes": total_likes})


def likes_distribution(request):
    distribution = (
        VacationLike.objects.filter(is_like=True)
        .values("vacation__title")
        .annotate(like_count=Count("id"))
        .order_by("-like_count")
    )

    data = [
        {"destination": item["vacation__title"], "likes": item["like_count"]}
        for item in distribution
    ]
    return JsonResponse(data, safe=False)


def vacations_per_country(request):
    sql = """
        SELECT c.name AS country, COUNT(v.id) AS count
        FROM vacations_vacation v
        JOIN vacations_country c ON v.country_id = c.id
        GROUP BY c.name
        ORDER BY c.name;
    """
    with connection.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()

    data = [{"country": r[0], "count": int(r[1])} for r in rows]
    return JsonResponse(data, safe=False)
