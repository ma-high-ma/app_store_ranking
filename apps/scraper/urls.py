from django.urls import path

from apps.scraper.views.app_ranking import AppRankingView, AppRankingResponseView

urlpatterns = [
    path('app-ranking/', AppRankingView.as_view(), name='html-home-page'),
    path('app-ranking-response/', AppRankingResponseView.as_view(), name='html-home-page'),
    ]
