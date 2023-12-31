# Generated by Django 4.2.3 on 2023-11-01 16:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ParkingSpot",
            fields=[
                (
                    "spotid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("isempty", models.BooleanField(default=True)),
                ("occupied_start_time", models.DateTimeField(blank=True, null=True)),
                (
                    "occupied_duration",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                ("user_name", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
