# Generated by Django 4.2.6 on 2023-11-17 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_alter_studentprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'male'), ('FEMALE', 'female')], default='male', max_length=50, null=True),
        ),
    ]
