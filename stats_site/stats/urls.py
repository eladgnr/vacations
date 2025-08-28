from django.urls import path
from . import views

urlpatterns = [
    path('stats-homepage/', views.stats_homepage, name='stats_homepage'),
    path('login/', views.login_view, name='stats_login'),
    path('logout/', views.logout_view, name='stats_logout'),

    # existing stats pages
    path('stats-vacations-per-country/', views.vacations_per_country_page,
         name='stats_vacations_per_country'),
    path('stats-vacations-overdue/', views.vacations_overdue_page,
         name='stats_vacations_overdue'),

    # new likes page
    path('stats-likes/', views.likes_page, name='stats_likes'),

    # new top likes page
    path('stats-top-likes/', views.top_likes_page, name='stats_top_likes'),

    # APIs
    path('api/vacations-per-country/', views.vacations_per_country_api,
         name='vacations_per_country_api'),
    path('api/vacations-overdue/', views.vacations_overdue_api,
         name='vacations_overdue_api'),
    path('api/likes-total/', views.likes_total_api, name='likes_total_api'),
    path('api/likes-per-country/', views.likes_per_country_api,
         name='likes_per_country_api'),
    path('api/likes-per-vacation/', views.likes_per_vacation_api,
         name='likes_per_vacation_api'),
]
