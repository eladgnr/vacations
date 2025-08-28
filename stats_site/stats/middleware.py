from django.shortcuts import redirect
from django.http import JsonResponse


class StatsLoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/api/") and not request.user.is_authenticated:
            return JsonResponse({"error": "please login first"}, status=403)
        return self.get_response(request)
