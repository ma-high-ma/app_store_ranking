from django.contrib import admin

# Register your models here.
from apps.scraper.models import BrowseAppsPageHtml, ShopifyApps, AppDelta


@admin.register(BrowseAppsPageHtml)
class BrowseAppsPageHtmlAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_no', 'created_at')


@admin.register(ShopifyApps)
class ShopifyAppsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rank', 'reviews_count', 'reviews_rating', 'created_at')
    ordering = ('rank',)


@admin.register(AppDelta)
class AppDeltaAdmin(admin.ModelAdmin):
    list_display = ('id', 'app', 'previous_rank', 'new_rank', 'rank_delta', 'created_at')
    ordering = ('rank_delta',)
