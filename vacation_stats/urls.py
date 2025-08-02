from django.urls import path
from .views import stats_summary

urlpatterns = [
    path('api/vacation-stats/', stats_summary, name='vacation_stats_summary'),
]
