# Generated by Django 4.2.6 on 2023-11-17 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_rename_surname_studentprofile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('FEMALE', 'female'), ('MALE', 'male')], default='male', max_length=50, null=True),
        ),
    ]