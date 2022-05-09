from django.test import TestCase
from news.forms import ArticleForm, RegisterUserForm, LoginUserForm


class ArticleFormTest(TestCase):
    def test_article_form_fields_label(self):
        form = ArticleForm()
        self.assertTrue(form.fields['title'].label == "Название")
        self.assertTrue(form.fields['anons'].label == "Аннонс")
        self.assertTrue(form.fields['date'].label == "Дата публикации")
        self.assertTrue(form.fields['full_text'].label == "Статья")


class RegisterFormTest(TestCase):
    def test_register_form_fields_label(self):
        form = RegisterUserForm()
        self.assertTrue(form.fields['username'].label == "Логин")
        self.assertTrue(form.fields['password1'].label == "Пароль")
        self.assertTrue(form.fields['password2'].label == "Повтор пароля")


class LoginFormTest(TestCase):
    def test_register_form_fields_label(self):
        form = LoginUserForm()
        self.assertTrue(form.fields['username'].label == "Логин")
        self.assertTrue(form.fields['password'].label == "Пароль")
