from django.contrib import admin
from django.urls import path, include
from vacations.views import custom_logout_view   # <-- import your view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ use custom logout
    path("accounts/logout/", custom_logout_view, name="logout"),

    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('vacations.urls')),
    path('api/', include('vacations.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
