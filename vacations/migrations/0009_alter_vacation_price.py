# Generated by Django 5.2.1 on 2025-06-26 15:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0008_vacation_end_date_vacation_price_vacation_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(10000.0)]),
        ),
    ]
