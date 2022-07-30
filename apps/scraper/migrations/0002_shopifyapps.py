# Generated by Django 4.0.6 on 2022-07-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopifyApps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=500)),
                ('developed_by', models.CharField(default='', max_length=500)),
                ('pricing_format', models.CharField(default='', max_length=500)),
                ('reviews_rating', models.IntegerField(default=0)),
                ('reviews_count', models.IntegerField(default=0)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('signifiers', models.JSONField(default=dict)),
                ('extras', models.JSONField(default=dict)),
            ],
            options={
                'unique_together': {('name', 'developed_by')},
            },
        ),
    ]
