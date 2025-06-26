from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class HomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

    def test_home_view_guest_access(self):
        """Guests should see the landing page"""
        self.client.logout()  # Ensure logged out
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacations/landing.html')

    def test_home_view_authenticated_user(self):
        """Logged-in users should see the vacation home page"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacations/home.html')
