# Generated by Django 3.0.14 on 2023-03-23 00:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crimsonboard', '0003_courses_enrollments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='userData',
        ),
    ]
