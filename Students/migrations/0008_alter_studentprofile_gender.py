# Generated by Django 4.2.6 on 2023-11-22 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0007_alter_studentprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female')], default='male', max_length=50),
        ),
    ]
