from django.shortcuts import render
import logging


# Create your views here.
def index(request):
    logging.info("index")
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)


def about(request):
    logging.info("about")
    return render(request, 'main/about.html')
