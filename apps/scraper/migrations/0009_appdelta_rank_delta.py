# Generated by Django 4.0.6 on 2022-07-31 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0008_alter_shopifyapps_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='appdelta',
            name='rank_delta',
            field=models.FloatField(default=0.0),
        ),
    ]
