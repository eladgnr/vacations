from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Vacation, Country
from datetime import date

"""
Unit and integration tests for the Vacations app.
"""


class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class AuthenticatedViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')

    def test_protected_view_requires_login(self):
        # Access without login → should redirect to login
        response = self.client.get('/my-vacations/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

        # Login and access again
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/my-vacations/')
        self.assertEqual(response.status_code, 200)


class APITest(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.country = Country.objects.create(name="Test Country")

        # Create vacation with all required fields
        self.vacation = Vacation.objects.create(
            title="Test Vacation",
            description="A test vacation",
            country=self.country,
            start_date=date(2025, 6, 1),
            end_date=date(2025, 6, 10),
            price=500.00
        )

    def test_get_vacations_api(self):
        response = self.api_client.get('/api/vacations/')
        self.assertEqual(response.status_code, 200)
        # Check if response contains data
        self.assertTrue(len(response.data) > 0)

    def test_vacations_per_country_api(self):
        response = self.api_client.get('/api/vacations-per-country/')
        self.assertEqual(response.status_code, 200)

    def test_overdue_vacations_api(self):
        response = self.api_client.get('/api/vacations-overdue/')
        self.assertEqual(response.status_code, 200)

    def test_likes_distribution_api(self):
        response = self.api_client.get('/api/likes/distribution/')
        self.assertEqual(response.status_code, 200)
