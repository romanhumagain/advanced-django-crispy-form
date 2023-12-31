# Generated by Django 4.2.1 on 2023-09-03 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_candidate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='experience',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidate',
            name='gender',
            field=models.CharField(default=datetime.datetime(2023, 9, 3, 15, 31, 14, 872265, tzinfo=datetime.timezone.utc), max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='salary',
            field=models.CharField(default=datetime.datetime(2023, 9, 3, 15, 31, 26, 345253, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
