from django.urls import path
from . import views
from .views import VacationUpdateView

urlpatterns = [
    path('', views.home, name='home'),
    path('country/<str:country_name>/', views.country_detail,
         name='country_detail'),
    path('vacation/<int:pk>/edit/', VacationUpdateView.as_view(),
         name='vacation_edit'),  # ✅ Add this
]
