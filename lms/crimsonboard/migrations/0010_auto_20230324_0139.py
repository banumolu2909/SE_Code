# Generated by Django 3.0.14 on 2023-03-24 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimsonboard', '0009_auto_20230324_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollments',
            name='course_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='enrollments',
            name='user',
            field=models.IntegerField(),
        ),
    ]
