from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

""" Tests for the home view of the vacations app.
This module contains tests for the home view, ensuring that both
guests and authenticated users can access the page correctly.
"""


class HomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

    def test_home_view_guest_access(self):
        """Guests should see the landing page"""
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacations/home.html')

    def test_home_view_authenticated_user(self):
        """Logged-in users should see the vacation home page"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacations/home.html')
