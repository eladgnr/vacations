from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

""" URL configuration for the vacation site project.
This module defines the URL patterns for the project, including admin, authentication,
and app-specific URLs.
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('vacations.urls')),
    path('api/', include('vacations.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
