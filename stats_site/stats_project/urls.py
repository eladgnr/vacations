from django.urls import path
from django.contrib.auth import views as auth_views
from stats import views   # import views from stats app

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    # Login/Logout
    path(
        "stats-login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            next_page="/stats-login/"),  # 👈 explicit redirect
        name="logout",
    ),
]
