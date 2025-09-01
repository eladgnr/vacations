from django.contrib import admin
from django.urls import path, include
from vacations.views import custom_logout_view
from django.conf import settings
from django.conf.urls.static import static
from vacations import views  # ✅ Import from your main vacations app

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/logout/", custom_logout_view, name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('vacations.urls')),
    path('api/', include('vacations.api_urls')),
    path("api/vacations-overdue/", views.vacations_overdue_api,
         name="vacations-overdue"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
