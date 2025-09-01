import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json


@login_required
def whoami(request):
    return JsonResponse({
        "user_id": request.user.id,
        "username": request.user.username,
        "email": request.user.email,
        "is_staff": request.user.is_staff,
        "is_superuser": request.user.is_superuser,
    })


def top_likes(request):
    resp = requests.get("http://web:8000/api/likes/distribution/")
    return JsonResponse(resp.json(), safe=False)


def likes_total(request):
    resp = requests.get("http://web:8000/api/likes/total/")
    return JsonResponse(resp.json(), safe=False)


def likes_per_country(request):
    resp = requests.get("http://web:8000/api/likes/per-country/")
    return JsonResponse(resp.json(), safe=False)


def likes_per_vacation(request):
    resp = requests.get("http://web:8000/api/likes/per-vacation/")
    return JsonResponse(resp.json(), safe=False)


def vacations_per_country(request):
    resp = requests.get("http://web:8000/api/vacations-per-country/")
    return JsonResponse(resp.json(), safe=False)


def vacations_overdue(request):
    try:
        resp = requests.get("http://web:8000/api/vacations-overdue/")
        print(f"Status code: {resp.status_code}")
        print(f"Response text: {resp.text}")

        if resp.status_code == 200:
            return JsonResponse(resp.json(), safe=False)
        else:
            return JsonResponse({"error": f"API returned status {resp.status_code}", "details": resp.text}, status=500)
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Response content: {resp.text}")
        return JsonResponse({"error": "Invalid JSON response", "content": resp.text}, status=500)
    except Exception as e:
        print(f"Request failed: {e}")
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def custom_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            identifier = data.get("username")
            password = data.get("password")

            user = authenticate(username=identifier, password=password)

            if user is None:
                from django.contrib.auth.models import User
                try:
                    u = User.objects.get(email=identifier)
                    user = authenticate(username=u.username, password=password)
                except User.DoesNotExist:
                    pass

            if user:
                login(request, user)
                return JsonResponse({"status": "ok", "user_id": user.id})
            else:
                return JsonResponse({"status": "error", "message": "Invalid credentials"}, status=401)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)


def custom_logout(request):
    logout(request)
    return JsonResponse({"status": "ok"})
