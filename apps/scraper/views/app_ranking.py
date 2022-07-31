from datetime import timedelta

from django.http import HttpResponse
from django.template import loader
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.utils.timezone import make_aware

from rest_framework.views import APIView


# def index(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())
from apps.scraper.services.app_ranking import AppRankingService


class AppRankingView(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'index.html'

    def get(self, request):
        app_name = request.GET.get('app_name')
        dev_by = request.GET.get('dev_by')
        start_date = request.GET.get('start_date', '2022-07-22')
        end_date = request.GET.get('end_date', '2022-07-31')
        print('REQUEST RESPONSE = ', request.GET)
        start_date = AppRankingService.convert_time_to_datetime(start_date)
        end_date = AppRankingService.convert_time_to_datetime(end_date)
        end_date = end_date + timedelta(days=1)
        img = AppRankingService().get_app_rank_data(
            app_name=app_name,
            dev_by=dev_by,
            start_date=start_date,
            end_date=end_date
        )

        return Response()

# class AppRankingResponseView(APIView):
#
