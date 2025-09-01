from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class VacationViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_home_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_loads(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_login_required_for_booking(self):
        response = self.client.get('/my-vacations/')
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_api_vacations_endpoint(self):
        response = self.client.get('/api/vacations/')
        self.assertEqual(response.status_code, 200)
