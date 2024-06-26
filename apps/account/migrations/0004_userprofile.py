# Generated by Django 5.0.6 on 2024-05-24 15:02

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile_picture', models.FileField(blank=True, null=True, upload_to='profile_picture/')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('school_college', models.CharField(blank=True, max_length=100, null=True)),
                ('major', models.CharField(blank=True, max_length=100, null=True)),
                ('year_of_study', models.CharField(blank=True, max_length=10, null=True)),
                ('graduation_year', models.CharField(blank=True, max_length=10, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
