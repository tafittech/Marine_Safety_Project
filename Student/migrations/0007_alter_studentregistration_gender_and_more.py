# Generated by Django 4.2.6 on 2023-11-09 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_alter_studentprofile_managers'),
        ('Student', '0006_studentregistration_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='gender',
            field=models.CharField(choices=[('FEMALE', 'female'), ('MALE', 'male')], default='male', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='student_type',
            field=models.CharField(choices=[('FOREIGNER', 'foreigner'), ('LOCAL', 'local')], default='local', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Admin.studentprofile'),
        ),
    ]
