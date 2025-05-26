from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name


class Vacation(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='vacations')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='vacation_images/', blank=True)

    def __str__(self):
        return f"{self.title} ({self.country.name})"


class VacationBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacation = models.ForeignKey('Vacation', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    room_type = models.IntegerField(choices=[
        (1, 'Single'),
        (2, 'Double'),
        (4, 'Family'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.vacation.title} ({self.start_date} to {self.end_date})"


class VacationBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacation = models.ForeignKey('Vacation', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    room_type = models.IntegerField(choices=[
        (1, 'Single'),
        (2, 'Double'),
        (4, 'Family'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.vacation.title} ({self.start_date} to {self.end_date})"
