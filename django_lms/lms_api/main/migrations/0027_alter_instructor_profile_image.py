# Generated by Django 4.1.7 on 2023-04-19 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_instructor_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='instructor_profile_imgs/'),
        ),
    ]
