# Generated by Django 4.2.6 on 2023-11-05 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_alter_studentprofile_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('Admin.user',),
        ),
    ]