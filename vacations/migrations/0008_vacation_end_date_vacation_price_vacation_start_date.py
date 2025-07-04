# Generated by Django 5.2.1 on 2025-06-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0007_alter_vacationbooking_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacation',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vacation',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='vacation',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
