# Generated by Django 5.1.2 on 2024-10-28 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        blank=True,
                        help_text="Введите место выполнения привычки",
                        max_length=256,
                        null=True,
                        verbose_name="Место",
                    ),
                ),
                (
                    "time",
                    models.TimeField(
                        help_text="Введите время выполнения привычки",
                        verbose_name="Время",
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        help_text="Введите действие, которое нужно выполнить",
                        max_length=256,
                        verbose_name="Действие",
                    ),
                ),
                (
                    "is_pleasant_habit",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "periodicity",
                    models.PositiveSmallIntegerField(
                        default=1,
                        help_text="Периодичность выполнения привычки для напоминания",
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "award",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "execution_time",
                    models.PositiveSmallIntegerField(
                        default=120,
                        help_text="Временя на выполнение полезной привычки в секундах ",
                        verbose_name="Длительность выполнения",
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=True, verbose_name="Признак публичности"
                    ),
                ),
                (
                    "associated_habit",
                    models.ForeignKey(
                        blank=True,
                        help_text="Данные признак указывается только для Полезной привычки",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная приятная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]