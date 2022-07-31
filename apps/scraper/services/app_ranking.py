import pytz
from matplotlib import pyplot
from apps.scraper.models import AppDelta, ShopifyApps
import datetime
class AppRankingService:
    def get_app_rank_data(self, app_name, dev_by, start_date, end_date):
        print('hey am inside the service file')

        result = []
        shopify_apps_rank = ShopifyApps.objects.filter(
            name=app_name,
            developed_by=dev_by,
            created_at__range=[start_date, end_date]
        ).values_list('rank', 'created_at')
        for i in shopify_apps_rank:
            x = {
                'app_name': app_name,
                'dev_by': dev_by,
                'rank': i[0],
                'created_at': i[1]
            }
            result.append(x)
        print('RESULT = ', result)

        print('Ranks = ', shopify_apps_rank)
        return result

        # return self.plot_graph(qs=shopify_apps_rank, app_name=app_name)


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
