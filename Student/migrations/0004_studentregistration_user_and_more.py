# Generated by Django 4.2.6 on 2023-11-05 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_alter_studentprofile_managers'),
        ('Student', '0003_alter_studentregistration_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistration',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.studentprofile'),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='gender',
            field=models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female')], default='male', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='student_type',
            field=models.CharField(choices=[('LOCAL', 'local'), ('FOREIGNER', 'foreigner')], default='local', max_length=50),
        ),
    ]
