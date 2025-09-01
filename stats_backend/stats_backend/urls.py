from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("whoami", views.whoami, name="whoami"),
    path("custom_login", views.custom_login, name="custom_login"),
    path("custom_logout", views.custom_logout, name="custom_logout"),

    # Stats endpoints
    path("vacations-per-country", views.vacations_per_country,
         name="vacations_per_country"),
    path("vacations-overdue", views.vacations_overdue, name="vacations_overdue"),

    # Likes endpoints
    path("likes/total/", views.likes_total, name="likes_total"),
    path("likes/per-country/", views.likes_per_country, name="likes_per_country"),
    path("likes/per-vacation/", views.likes_per_vacation,
         name="likes_per_vacation"),
    path("top-likes", views.top_likes, name="top_likes"),
]
