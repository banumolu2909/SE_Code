# Generated by Django 4.1.7 on 2023-04-16 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_instructor_login_time_instructor_logout_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor_courses', to='main.instructor'),
        ),
    ]
