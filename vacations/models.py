from django.db import models


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
