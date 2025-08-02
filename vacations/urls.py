from django.urls import path
from . import views
from .views import VacationUpdateView
from vacations import views
from django.urls import path, include

""" URL patterns for the Vacations app.
This module defines the URL patterns for the Vacations app, including views for"""

urlpatterns = [
    path('', views.home, name='home'),  # ✅ homepage
    path('register/', views.register, name='register'),
    path('country/<str:country_name>/',
         views.country_detail, name='country_detail'),
    path('vacation/<int:pk>/edit/',
         VacationUpdateView.as_view(), name='vacation_edit'),
    path('vacation/<int:vacation_id>/choose/',
         views.choose_vacation, name='choose_vacation'),
    path('my-vacations/', views.my_vacations, name='my_vacations'),
    path('vacations/<int:vacation_id>/like/',
         views.vacation_like, name='vacation_like'),
    path('vacation/delete/<int:vacation_id>/',
         views.delete_vacation, name='delete_vacation'),
    path('vacation/order/<int:vacation_id>/',
         views.order_vacation, name='order_vacation'),
    path('add-vacation/', views.add_vacation, name='add_vacation'),
    path('', include('vacation_stats.urls')),

]
