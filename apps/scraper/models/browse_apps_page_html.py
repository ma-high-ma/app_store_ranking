from django.db import models


class BrowseAppsPageHtml(models.Model):
    page_no = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
