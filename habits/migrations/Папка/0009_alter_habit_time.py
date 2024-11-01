# Generated by Django 5.1.2 on 2024-10-31 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0008_alter_habit_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="time",
            field=models.TimeField(
                help_text="Введите время выполнения привычки",
                verbose_name="Время, когда нужно выполнить привычку",
            ),
        ),
    ]
