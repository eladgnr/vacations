from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # no logout_view here anymore — handled in stats_project/urls.py
]
