from django.test import TestCase
from news.models import Author, Articles
from django.urls import reverse

from django.utils import timezone

now = timezone.now()
today = timezone.now().date()


class AuthorViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_authors = 10
        for author_num in range(number_of_authors):
            Author.objects.create(name=f"Dima {author_num}")

    def test_view_url_exists_at_desired_location_author(self):
        resp = self.client.get('/news/authors_name/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_author(self):
        resp = self.client.get(reverse('authors_name'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_author(self):
        resp = self.client.get(reverse('authors_name'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'news/author_names.html')

    def test__all_authors(self):
        resp = self.client.get(reverse('authors_name'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['authors']) == 10)

    def test_one_author(self):
        resp = self.client.get(reverse('authors_name') + '6')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['authors']) == 1)


class ArticlesViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_articles = 10
        for article_num in range(number_of_articles):
            Articles.objects.create(title=f"First {article_num}", anons="asd", full_text="asdf", date=now)

    def test_view_url_exists_at_desired_location_article(self):
        resp = self.client.get('/news/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_article(self):
        resp = self.client.get(reverse('news_home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_article(self):
        resp = self.client.get(reverse('news_home'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'news/news_home.html')

    def test__all_articles(self):
        resp = self.client.get(reverse('news_home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['news']) == 10)

    def test_one_article(self):
        resp = self.client.get(reverse('news_home') + '6')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(str(resp.context['article']) == "First 5")


class LoginViewTest(TestCase):
    def test_view_url_exists_at_desired_location_login(self):
        resp = self.client.get('/news/login/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_login(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_login(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'news/login.html')


class RegisterViewTest(TestCase):
    def test_view_url_exists_at_desired_location_register(self):
        resp = self.client.get('/news/register/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_register(self):
        resp = self.client.get(reverse('register'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_register(self):
        resp = self.client.get(reverse('register'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'news/register.html')
