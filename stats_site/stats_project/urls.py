from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('stats_homepage')),
    path('', include('stats.urls')),
]
