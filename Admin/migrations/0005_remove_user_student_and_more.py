# Generated by Django 4.2.6 on 2023-11-17 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_studentprofile_studentemergencyprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='student',
        ),
        migrations.AlterField(
            model_name='studentemergencyprofile',
            name='emergency_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='messages', to='Admin.studentprofile'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'male'), ('FEMALE', 'female')], default='male', max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('student', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('Admin.user',),
            managers=[
                ('students', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.studentuser'),
        ),
    ]