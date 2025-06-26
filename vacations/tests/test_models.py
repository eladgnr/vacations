from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from vacations.models import Country, Vacation, VacationBooking, VacationLike
from datetime import date, timedelta


class VacationModelTests(TestCase):

    def setUp(self):
        self.country = Country.objects.create(name="Spain")
        self.user = User.objects.create_user(
            username="elad", password="pass123")

    def test_vacation_price_validation(self):
        vacation = Vacation(
            country=self.country,
            title="Cheap Trip",
            description="Test",
            price=-5.00,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=5)
        )
        with self.assertRaises(ValidationError):
            vacation.full_clean()

    def test_vacation_date_validation(self):
        vacation = Vacation(
            country=self.country,
            title="Reverse Dates",
            price=100.00,
            start_date=date.today() + timedelta(days=5),
            end_date=date.today()
        )
        with self.assertRaises(ValidationError):
            vacation.full_clean()

    def test_vacation_str(self):
        vacation = Vacation.objects.create(
            country=self.country,
            title="Barcelona Tour",
            price=500.00,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=2)
        )
        self.assertEqual(str(vacation), "Barcelona Tour (Spain)")


class VacationBookingTests(TestCase):

    def setUp(self):
        self.country = Country.objects.create(name="Italy")
        self.user = User.objects.create_user(
            username="tester", password="testpass")
        self.vacation = Vacation.objects.create(
            country=self.country,
            title="Rome",
            price=1000.00,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=2)
        )

    def test_vacation_booking_str(self):
        booking = VacationBooking.objects.create(
            user=self.user,
            vacation=self.vacation,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=1),
            room_type=2
        )
        self.assertIn("tester - Rome", str(booking))


class VacationLikeTests(TestCase):

    def setUp(self):
        self.country = Country.objects.create(name="Greece")
        self.user = User.objects.create_user(
            username="liker", password="likerpass")
        self.vacation = Vacation.objects.create(
            country=self.country,
            title="Athens Trip",
            price=999.99,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=1)
        )

    def test_vacation_like_str(self):
        like = VacationLike.objects.create(
            user=self.user, vacation=self.vacation, is_like=True)
        self.assertEqual(str(like), "liker liked Athens Trip")

    def test_vacation_like_uniqueness(self):
        VacationLike.objects.create(
            user=self.user, vacation=self.vacation, is_like=True)
        # IntegrityError or ValidationError depending on DB/backend
        with self.assertRaises(Exception):
            VacationLike.objects.create(
                user=self.user, vacation=self.vacation, is_like=False)
