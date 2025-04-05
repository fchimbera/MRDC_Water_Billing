# Generated by Django 5.1.6 on 2025-04-05 21:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bills', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meterreading',
            name='account',
            field=models.ForeignKey(db_column='account_id', on_delete=django.db.models.deletion.CASCADE, related_name='meter_readings', to=settings.AUTH_USER_MODEL, to_field='account_id'),
        ),
        migrations.AddField(
            model_name='bill',
            name='meter_reading',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.meterreading'),
        ),
        migrations.AddField(
            model_name='bill',
            name='rate_used',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bills.waterrate'),
        ),
    ]
