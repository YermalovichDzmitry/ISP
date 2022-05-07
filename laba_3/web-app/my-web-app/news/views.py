from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import Articles, Category, Author
from .forms import ArticleForm, RegisterUserForm, LoginUserForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, filemode="w")


def authors_name(request):
    authors = Author.objects.all()
    data = {
        "authors": authors
    }
    return render(request, 'news/author_names.html', data)


def news_home(request):
    logging.info("news_home")
    news = Articles.objects.all()
    cats = Category.objects.all()
    data = {
        'news': news,
        "cats": cats,
        "name_category": "Все категории",
    }
    return render(request, 'news/news_home.html', data)


class NewsUpdateView(UpdateView):
    logging.info("NewsUpdateView")
    model = Articles  # Модель
    template_name = 'news/create.html'  # Шаблон
    form_class = ArticleForm


class NewsDeleteView(DeleteView):
    logging.info("NewsDeleteView")
    model = Articles  # Модель
    success_url = '/news/'
    template_name = 'news/news-delete.html'  # Шаблон


class NewDetailView(DetailView):
    logging.info("NewDetailView")
    model = Articles  # Модель
    template_name = 'news/details_view.html'  # Шаблон
    context_object_name = 'article'  # С помощью чего передаём данные


def create(request):
    logging.info("create")
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


def show_category(request, cat_id):
    logging.info("show_category")
    news = Articles.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    data = {
        'news': news,
        "cats": cats,
        "name_category": "Все категории"
    }
    return render(request, 'news/news_home.html', data)


def show_authors(request, authors_id):
    authors = Author.objects.filter(id=authors_id)
    data = {
        "authors": authors
    }
    return render(request, 'news/author_details.html', data)



class RegisterUser(CreateView):
    logging.info("RegisterUser")
    form_class = RegisterUserForm
    template_name = 'news/register.html'
    success_url = reverse_lazy("login")


class LoginUser(LoginView):
    logging.info("LoginUser")
    form_class = LoginUserForm
    template_name = 'news/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logging.info("logout_user")
    logout(request)
    return redirect('login')
