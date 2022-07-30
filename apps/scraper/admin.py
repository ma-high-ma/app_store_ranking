from django.contrib import admin

# Register your models here.
from apps.scraper.models import BrowseAppsPageHtml


@admin.register(BrowseAppsPageHtml)
class BrowseAppsPageHtmlAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_no', 'created_at')
