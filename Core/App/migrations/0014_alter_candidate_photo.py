# Generated by Django 4.2.1 on 2023-09-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_candidate_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='photo',
            field=models.ImageField(upload_to='candidate_photo'),
        ),
    ]
