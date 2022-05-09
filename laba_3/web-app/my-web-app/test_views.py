from django.test import TestCase
from news.models import Author
from django.urls import reverse


class AuthorListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_authors = 13
        for author_num in range(number_of_authors):
            Author.objects.create(name=f"Dima {author_num}")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/news/authors_name/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('authors_name'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('authors_name'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'news/author_names.html')
