# Generated by Django 4.2.6 on 2023-11-22 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0010_alter_studentprofile_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='student_type',
            field=models.CharField(choices=[('LOCAL', 'local'), ('FOREIGNER', 'foreigner')], default='local', max_length=50),
        ),
    ]
