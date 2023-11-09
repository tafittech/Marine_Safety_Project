# Generated by Django 4.2.6 on 2023-11-09 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_image', models.ImageField(blank=True, default='default1.jpeg', null=True, upload_to='')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female')], default='male', max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('student_type', models.CharField(choices=[('LOCAL', 'local'), ('FOREIGNER', 'foreigner')], default='local', max_length=50)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('national_id', models.CharField(blank=True, max_length=255, null=True)),
                ('birth_cert_number', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('employer', models.CharField(blank=True, max_length=255, null=True)),
                ('employer_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('student', models.BooleanField(default=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
