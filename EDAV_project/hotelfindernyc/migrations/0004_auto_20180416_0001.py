# Generated by Django 2.0 on 2018-04-16 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelfindernyc', '0003_auto_20180414_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='latitude',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='hotel',
            name='longitude',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
