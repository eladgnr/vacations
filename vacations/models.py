from django.contrib.auth.models import User  # Make sure this is at the top
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name


class Vacation(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='vacations')
    title = models.CharField(max_length=200)  # ✅ required
    description = models.TextField()          # ✅ required (remove blank=True)
    image = models.ImageField(
        upload_to='vacation_images/', blank=True)  # ✅ optional

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01),
            MaxValueValidator(10000.00)
        ]
    )
    start_date = models.DateField()  # ✅ required (remove null=True, blank=True)
    end_date = models.DateField()    # ✅ required (remove null=True, blank=True)

    def clean(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValidationError(
                "End date cannot be earlier than start date.")

    def __str__(self):
        return f"{self.title} ({self.country.name})"


class VacationBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacation = models.ForeignKey('Vacation', on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)   # ✅ optional
    end_date = models.DateField(null=True, blank=True)     # ✅ optional
    room_type = models.IntegerField(
        choices=[
            (1, 'Single'),
            (2, 'Double'),
            (4, 'Family'),
        ],
        null=True,      # ✅ allow null in database
        blank=True      # ✅ allow blank in forms
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.vacation.title} ({self.start_date} to {self.end_date})"


class VacationLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacation = models.ForeignKey(Vacation, on_delete=models.CASCADE)
    is_like = models.BooleanField()  # True = like, False = unlike

    class Meta:
        # Prevent multiple likes/unlikes per vacation per user
        unique_together = ('user', 'vacation')

    def __str__(self):
        return f"{self.user.username} {'liked' if self.is_like else 'unliked'} {self.vacation.title}"
