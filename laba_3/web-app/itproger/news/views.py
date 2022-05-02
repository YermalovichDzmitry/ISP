from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsUpdateView(UpdateView):
    model = Articles  # Модель
    template_name = 'news/create.html'  # Шаблон
    form_class = ArticleForm


class NewsDeleteView(DeleteView):
    model = Articles  # Модель
    success_url = '/news/'
    template_name = 'news/news-delete.html'  # Шаблон


class NewDetailView(DetailView):
    model = Articles  # Модель
    template_name = 'news/details_view.html'  # Шаблон
    context_object_name = 'article'  # С помощью чего передаём данные


def create(request):
    error = ''
    if request.method == "POST":  # То есть пользователь нажал на кнопку добавить статью
        form = ArticleForm(request.POST)  # Данные полученные от пользователя из формы
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была не верной"
    form = ArticleForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
