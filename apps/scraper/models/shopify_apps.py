from django.db import models


class ShopifyApps(models.Model):
    rank = models.IntegerField(default=0)
    name = models.CharField(default='', max_length=500)
    developed_by = models.CharField(default='', max_length=500)
    pricing_format = models.CharField(default='', max_length=500)
    reviews_rating = models.FloatField(default=0.0)
    reviews_count = models.IntegerField(default=0)
    modified_at = models.DateTimeField(auto_now_add=True)
    signifiers = models.JSONField(default=dict)
    extras = models.JSONField(default=dict)

    class Meta:
        unique_together = ('name', 'developed_by')