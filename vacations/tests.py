from django.test import TestCase
from .models import Vacation, Country
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Vacation

# Test That Does NOT Require Login


def test_home_page_redirects_to_login(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 302)
    self.assertIn('/accounts/login/', response.url)


# Test That Requires Login
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

# DRF Test Using APIClient


class APITest(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.country = Country.objects.create(name="Test Country")

        self.vacation = Vacation.objects.create(
            title="Test Vacation",
            description="A test vacation",
            country=self.country
        )

    def test_get_vacations_api(self):
        response = self.api_client.get('/api/vacations/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], "Test Vacation")
