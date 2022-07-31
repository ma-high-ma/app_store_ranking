import datetime

from django.db import models


class ShopifyApps(models.Model):
    rank = models.IntegerField(default=0)
    name = models.CharField(default='', max_length=500)
    developed_by = models.CharField(default='', max_length=500)
    pricing_format = models.CharField(default='', max_length=500)
    reviews_rating = models.FloatField(default=0.0)
    reviews_count = models.IntegerField(default=0)
    modified_at = models.DateTimeField(auto_now=True)
    signifiers = models.JSONField(default=dict)
    extras = models.JSONField(default=dict)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        unique_together = ('name', 'developed_by', 'created_at')


