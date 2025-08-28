from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.db import connection
import datetime
from django.utils.timezone import now

# Homepage


def stats_homepage(request):
    return render(request, "stats_homepage.html")

# Login


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user and user.is_superuser:
            login(request, user)
            return redirect("stats_homepage")
        else:
            messages.error(request, "wrong creds, please check and retry")
            return redirect("stats_homepage")
    return redirect("stats_homepage")


def logout_view(request):
    logout(request)
    return redirect("stats_homepage")

# Pages for statistics


def vacations_per_country_page(request):
    if not request.user.is_authenticated:
        messages.error(request, "please login first")
        return redirect("stats_homepage")
    return render(request, "vacations_per_country.html")


def vacations_overdue_page(request):
    if not request.user.is_authenticated:
        messages.error(request, "please login first")
        return redirect("stats_homepage")
    return render(request, "vacations_overdue.html")

# APIs (for chart.js fetch)


def vacations_per_country_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "please login first"}, status=403)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.name, COUNT(v.id) 
            FROM vacations_vacation v
            JOIN vacations_country c ON v.country_id = c.id
            GROUP BY c.name
            ORDER BY c.name
        """)
        rows = cursor.fetchall()

    results = [{"country": row[0], "count": row[1]} for row in rows]
    return JsonResponse(results, safe=False)


def vacations_overdue_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "please login first"}, status=403)

    today = now().date()

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.name AS country, v.title AS city, v.start_date, v.end_date
            FROM vacations_vacation v
            JOIN vacations_country c ON v.country_id = c.id
            ORDER BY v.start_date ASC
        """)
        rows = cursor.fetchall()

    results = []
    for row in rows:
        country, city, start_date, end_date = row

        # Make sure these are dates
        if hasattr(start_date, "date"):
            start_date = start_date.date()
        if hasattr(end_date, "date"):
            end_date = end_date.date()

        status = "overdue" if end_date < today else "default"

        results.append({
            "country": country,
            "city": city,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "status": status
        })

    return JsonResponse(results, safe=False)


def likes_total_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "please login first"}, status=403)

    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM vacations_vacationlike")
        total = cursor.fetchone()[0]

    return JsonResponse({"total_likes": total})


def likes_per_country_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "please login first"}, status=403)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.name, COUNT(l.id) 
            FROM vacations_vacationlike l
            JOIN vacations_vacation v ON l.vacation_id = v.id
            JOIN vacations_country c ON v.country_id = c.id
            GROUP BY c.name
            ORDER BY c.name
        """)
        rows = cursor.fetchall()

    results = [{"country": row[0], "likes": row[1]} for row in rows]
    return JsonResponse(results, safe=False)


def likes_page(request):
    if not request.user.is_authenticated:
        messages.error(request, "please login first")
        return redirect("stats_homepage")
    return render(request, "likes.html")


def likes_per_vacation_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "please login first"}, status=403)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT v.title AS city, c.name AS country, COUNT(l.id) AS likes
            FROM vacations_vacationlike l
            JOIN vacations_vacation v ON l.vacation_id = v.id
            JOIN vacations_country c ON v.country_id = c.id
            GROUP BY v.id, v.title, c.name
            ORDER BY likes DESC
        """)
        rows = cursor.fetchall()

    results = [{"city": row[0], "country": row[1], "likes": row[2]}
               for row in rows]
    return JsonResponse(results, safe=False)


def top_likes_page(request):
    if not request.user.is_authenticated:
        messages.error(request, "please login first")
        return redirect("stats_homepage")
    return render(request, "top_likes.html")
