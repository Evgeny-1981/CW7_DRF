# Generated by Django 5.1.2 on 2024-10-31 05:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0006_alter_habit_associated_habit"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="habit",
            name="is_public",
        ),
        migrations.AddField(
            model_name="habit",
            name="is_public_habit",
            field=models.BooleanField(
                default=True, verbose_name="Признак публичности привычки"
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="action",
            field=models.CharField(
                help_text="Введите действие, которое нужно выполнить",
                max_length=256,
                verbose_name="Действие, которое представляет собой привычка",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="associated_habit",
            field=models.ForeignKey(
                blank=True,
                help_text="Данные признак указывается только для полезной привычки",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="habits.habit",
                verbose_name="Связанная привычка",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="execution_time",
            field=models.PositiveSmallIntegerField(
                default=120,
                help_text="Временя на выполнение полезной привычки в секундах ",
                verbose_name="Длительность выполнения привычки",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Привычки",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель привычки",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="place",
            field=models.CharField(
                blank=True,
                help_text="Введите место выполнения привычки",
                max_length=256,
                null=True,
                verbose_name="Место, в котором необходимо выполнить привычку",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="time",
            field=models.TimeField(
                help_text="Введите время выполнения привычки",
                verbose_name="Время, когда нужно выполнить привычку",
            ),
        ),
    ]
