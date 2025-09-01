from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    VacationViewSet,
    vacations_stats,
    users_total,
    likes_total,
    likes_distribution,
    vacations_per_country,
)

router = DefaultRouter()
router.register(r'vacations', VacationViewSet)

urlpatterns = [
    path('vacations/stats/', vacations_stats, name='vacations-stats'),
    path('users/total/', users_total, name='users-total'),
    path('likes/total/', likes_total, name='likes-total'),
    path('likes/distribution/', likes_distribution, name='likes-distribution'),
    path('vacations-per-country/', vacations_per_country,
         name='vacations-per-country'),
    path('', include(router.urls)),
]


def likes_per_country(request):
    sql = """
        SELECT c.name AS country, COUNT(l.id) AS like_count
        FROM vacations_vacationlike l
        JOIN vacations_vacation v ON l.vacation_id = v.id
        JOIN vacations_country c ON v.country_id = c.id
        WHERE l.is_like = TRUE
        GROUP BY c.name
        ORDER BY c.name;
    """
    with connection.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()

    data = [{"country": r[0], "likes": int(r[1])} for r in rows]
    return JsonResponse(data, safe=False)
