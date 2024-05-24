# Generated by Django 5.0.6 on 2024-05-24 13:46

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_picture', models.FileField(blank=True, null=True, upload_to='')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('school_college', models.CharField(blank=True, max_length=100, null=True)),
                ('major', models.CharField(blank=True, max_length=100, null=True)),
                ('year_of_study', models.CharField(blank=True, max_length=10, null=True)),
                ('graduation_year', models.CharField(blank=True, max_length=10, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('account.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
