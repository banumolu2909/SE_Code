# Generated by Django 3.0.14 on 2023-03-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimsonboard', '0004_auto_20230322_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='role',
            field=models.CharField(choices=[('S', 'Student'), ('I', 'Instructor'), ('A', 'Admin')], default='S', max_length=1),
        ),
    ]