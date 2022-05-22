from django.shortcuts import render
import logging
from django.views import View

logger = logging.getLogger('main')


# Create your views here.
# def index(request):
#     logger.info("index")
#     data = {
#         'title': 'Главная страница',
#     }
#     return render(request, 'main/index.html', data)


class Index(View):
    def get(self, request):
        logger.info("Index")
        data = {
            'title': 'Главная страница',
        }
        return render(request, 'main/index.html', data)


class About(View):
    def get(self, request):
        logger.info("About")
        return render(request, 'main/about.html')

# def about(request):
#     logger.info("about")
#     return render(request, 'main/about.html')
