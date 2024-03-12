# Generated by Django 5.0.3 on 2024-03-12 17:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statuses', '0003_alter_statusdataset_data'),
        ('telemetry', '0003_alter_telemetrydataset_data'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('statuses', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flight_analytics', to='statuses.statusdataset', verbose_name='Status dataset')),
                ('telemetry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flight_analytics', to='telemetry.telemetrydataset', verbose_name='Telemetry dataset')),
            ],
            options={
                'verbose_name': 'Flight analytics',
                'verbose_name_plural': 'Flight analytics',
            },
        ),
    ]