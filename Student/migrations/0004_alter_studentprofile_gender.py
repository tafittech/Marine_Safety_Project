# Generated by Django 4.2.6 on 2023-11-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_alter_studentprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(choices=[('FEMALE', 'female'), ('MALE', 'male')], default='male', max_length=50),
        ),
    ]
