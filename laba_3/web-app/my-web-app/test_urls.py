from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import authors_name, news_home, NewsUpdateView, NewsDeleteView, NewDetailView, create, show_category, \
    show_authors, RegisterUser, LoginUser, logout_user


class TestUrls(SimpleTestCase):
    def test_authors_name_url_resolve(self):
        url = reverse("authors_name")
        self.assertEqual(resolve(url).func, authors_name)

    def test_news_home_name_url_resolve(self):
        url = reverse("news_home")
        self.assertEqual(resolve(url).func, news_home)

    def test_login_name_url_resolve(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func.view_class, LoginUser)

    def test_register_name_url_resolve(self):
        url = reverse("register")
        self.assertEqual(resolve(url).func.view_class, RegisterUser)

    def test_news_detail_name_url_resolve(self):
        url = reverse("news-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, NewDetailView)

    def test_news_update_name_url_resolve(self):
        url = reverse("news-update", args=[1])
        self.assertEqual(resolve(url).func.view_class, NewsUpdateView)

    def test_news_delete_name_url_resolve(self):
        url = reverse("news-delete", args=[1])
        self.assertEqual(resolve(url).func.view_class, NewsDeleteView)

    def test_create_url_resolve(self):
        url = reverse("create")
        self.assertEqual(resolve(url).func, create)

    def test_category_url_resolve(self):
        url = reverse("category", args=[1])
        self.assertEqual(resolve(url).func, show_category)

    def test_logout_url_resolve(self):
        url = reverse("logout")
        self.assertEqual(resolve(url).func, logout_user)

    def test_authors_detail_url_resolve(self):
        url = reverse("authors_detail", args=[1])
        self.assertEqual(resolve(url).func, show_authors)
