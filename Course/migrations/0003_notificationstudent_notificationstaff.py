# Generated by Django 4.2.6 on 2023-11-22 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0011_alter_studentprofile_student_type'),
        ('Admin', '0001_initial'),
        ('Course', '0002_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationStudent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_id', models.DateTimeField(auto_now_add=True)),
                ('updated_id', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.studentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationStaff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_id', models.DateTimeField(auto_now_add=True)),
                ('updated_id', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.adminprofile')),
            ],
        ),
    ]
