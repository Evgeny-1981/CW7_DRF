# Generated by Django 5.1.2 on 2024-10-30 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0003_alter_habit_table"),
    ]

    operations = [
        migrations.RenameField(
            model_name="habit",
            old_name="time",
            new_name="time_at",
        ),
    ]
