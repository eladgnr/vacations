"""
this module contains the API URLs for the vacations app.
It uses Django REST Framework's DefaultRouter to automatically generate
"""

# vacations/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import VacationViewSet

router = DefaultRouter()
router.register(r'vacations', VacationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
