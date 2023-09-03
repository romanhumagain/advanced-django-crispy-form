# Generated by Django 4.2.1 on 2023-09-03 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_alter_candidate_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='experience',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='salary',
            field=models.CharField(default=datetime.datetime(2023, 9, 3, 16, 19, 26, 821725, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
    ]
