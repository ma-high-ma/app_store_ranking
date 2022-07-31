import pytz
from matplotlib import pyplot
from apps.scraper.models import AppDelta, ShopifyApps
import datetime
class AppRankingService:
    def get_app_rank_data(self, app_name, dev_by, start_date, end_date):
        print('hey am inside the service file')
        # shopify_app_obj = ShopifyApps.objects.filter(name=app_name).first()
        # print('shopify obj = ', shopify_app_obj)
        # app_delta_qs = AppDelta.objects.filter(app_name=shopify_app_obj, created_at__in=(start_date, end_date))
        # app_delta_qs = AppDelta.objects.filter(app__name=app_name, created_at__range=[start_date, end_date])
        # print('app_delta_qs = ', app_delta_qs)
        # for app in app_delta_qs:
        #     print(app.__dict__)
        #     print('-----------------------------')

        shopify_apps_rank = ShopifyApps.objects.filter(
            name=app_name,
            developed_by=dev_by,
            created_at__range=[start_date, end_date]
        ).values_list('rank', 'created_at')
        for i in shopify_apps_rank:
            print(i)
        print('Ranks = ', shopify_apps_rank)
        return self.plot_graph(qs=shopify_apps_rank, app_name=app_name)

    def plot_graph(self, qs, app_name):
        ranks = list(map(lambda d: d[0], qs))
        dates = list(map(lambda d: d[1].day, qs))

        ranks_plot = pyplot.plot(dates, ranks, 'bo-', label=app_name)[0]

        pyplot.axis([min(dates)-5, 31, 1, 150])
        pyplot.xlabel('day')

        # Set up the legend and title
        pyplot.legend(handles=[ranks_plot])
        pyplot.title(f'{app_name}_rank')

        # Show the plot
        pyplot.show()

        img = pyplot.savefig('graph.png')
        return img


    @staticmethod
    def convert_time_to_datetime(time_data):
        t = datetime.datetime.strptime(time_data, "%Y-%m-%d")
        t = t.replace(tzinfo=datetime.timezone.utc)
        return t
