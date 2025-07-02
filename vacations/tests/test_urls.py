from django.test import SimpleTestCase
from django.urls import reverse, resolve
from vacations import views
from vacations.views import VacationUpdateView

# 

class UrlTests(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, views.register)

    def test_country_detail_url(self):
        url = reverse('country_detail', kwargs={'country_name': 'Spain'})
        self.assertEqual(resolve(url).func, views.country_detail)

    def test_vacation_edit_url(self):
        url = reverse('vacation_edit', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, VacationUpdateView)

    def test_choose_vacation_url(self):
        url = reverse('choose_vacation', kwargs={'vacation_id': 1})
        self.assertEqual(resolve(url).func, views.choose_vacation)

    def test_my_vacations_url(self):
        url = reverse('my_vacations')
        self.assertEqual(resolve(url).func, views.my_vacations)

    def test_like_url(self):
        url = reverse('vacation_like', kwargs={'vacation_id': 1})
        self.assertEqual(resolve(url).func, views.vacation_like)

    def test_delete_url(self):
        url = reverse('delete_vacation', kwargs={'vacation_id': 1})
        self.assertEqual(resolve(url).func, views.delete_vacation)

    def test_order_url(self):
        url = reverse('order_vacation', kwargs={'vacation_id': 1})
        self.assertEqual(resolve(url).func, views.order_vacation)
