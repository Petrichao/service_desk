# Generated by Django 5.0.2 on 2024-03-12 10:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]