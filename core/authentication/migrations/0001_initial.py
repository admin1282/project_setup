# Generated by Django 5.0.4 on 2024-11-27 15:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('domain', models.URLField()),
                ('year_founded', models.IntegerField()),
                ('industry', models.CharField(max_length=255)),
                ('size_range', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('linkedin_url', models.URLField()),
                ('current_employee_estimate', models.IntegerField()),
                ('total_employee_estimate', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
