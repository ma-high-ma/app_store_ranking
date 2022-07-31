
from django.db import models

from apps.scraper.models import ShopifyApps


class AppDelta(models.Model):
    app = models.ForeignKey(ShopifyApps, on_delete=models.CASCADE)
    previous_rank = models.FloatField()
    new_rank = models.FloatField()
    rank_delta = models.FloatField(default=0.0)
    app_previous_details = models.JSONField(default=dict)
    app_new_details = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
