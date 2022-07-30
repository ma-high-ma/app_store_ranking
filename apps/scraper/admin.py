from django.contrib import admin

# Register your models here.
from apps.scraper.models import BrowseAppsPageHtml, ShopifyApps


@admin.register(BrowseAppsPageHtml)
class BrowseAppsPageHtmlAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_no', 'created_at')

@admin.register(ShopifyApps)
class ShopifyAppsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rank', 'reviews_count', 'reviews_rating', 'modified_at')
    ordering = ('rank', )
