# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('event_name', models.CharField(max_length=75)),
                ('event_description', models.CharField(max_length=1000)),
                ('event_date', models.DateField()),
                ('event_timing', models.TimeField()),
                ('event_venue', models.CharField(max_length=100)),
                ('event_fees', models.IntegerField(default=0)),
                ('event_seats', models.IntegerField(default=30)),
                ('event_organiser_details', models.CharField(max_length=500)),
            ],
        ),
    ]
