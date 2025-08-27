from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import (
    VacationViewSet,
    vacations_stats,
    users_total,
    likes_total,
    likes_distribution,
    vacations_per_country
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
    path("likes-per-country/", views.likes_per_country, name="likes-per-country"),
]
