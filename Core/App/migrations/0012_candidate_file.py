# Generated by Django 4.2.1 on 2023-09-04 05:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_alter_candidate_experience_alter_candidate_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='file',
            field=models.FileField(default=datetime.datetime(2023, 9, 4, 5, 33, 52, 634573, tzinfo=datetime.timezone.utc), upload_to='candidate_files'),
            preserve_default=False,
        ),
    ]
