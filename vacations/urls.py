from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('country/<str:country_name>/', views.country_detail,
         name='country_detail'),  # ✅ Add this
]
