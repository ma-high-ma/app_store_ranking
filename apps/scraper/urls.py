from django.urls import path

from apps.scraper.views.app_ranking import AppRankingView

urlpatterns = [
    path('app-ranking/', AppRankingView.as_view(), name='html-home-page')
    ]
