from django.urls import path
from . import views
from .views import VacationUpdateView

urlpatterns = [
    path('', views.home, name='home'),  # ✅ homepage
    path('register/', views.register, name='register'),
    path('country/<str:country_name>/',
         views.country_detail, name='country_detail'),
    path('vacation/<int:pk>/edit/',
         VacationUpdateView.as_view(), name='vacation_edit'),
    path('vacation/<int:vacation_id>/choose/',
         views.choose_vacation, name='choose_vacation'),
]
