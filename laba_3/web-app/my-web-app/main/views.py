from django.shortcuts import render
import logging

logger = logging.getLogger('main')


# Create your views here.
def index(request):
    logger.info("index")
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)


def about(request):
    logger.info("about")
    return render(request, 'main/about.html')
