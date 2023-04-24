# Generated by Django 4.1.7 on 2023-04-22 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_instructorstudentchat'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(default='Bloomington', null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mobile_number',
            field=models.IntegerField(default=1234567890, null=True),
        ),
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('assignment_file', models.FileField(null=True, upload_to='assignments/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_assignments', to='main.course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.instructor')),
            ],
            options={
                'verbose_name_plural': '8. Assignments',
            },
        ),
        migrations.CreateModel(
            name='AssignmentResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reponse_text', models.TextField(default='Submission Done', null=True)),
                ('submission_file', models.FileField(null=True, upload_to='responses/')),
                ('submission_time', models.DateTimeField(auto_now_add=True)),
                ('grade', models.FloatField(default=0)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.assignments')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
            options={
                'verbose_name_plural': '9. Assignment Responses',
            },
        ),
    ]