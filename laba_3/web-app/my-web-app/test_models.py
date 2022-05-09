from django.test import TestCase

from news.models import Author


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='Dima', gender='M')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_gender_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('gender').verbose_name
        self.assertEquals(field_label, 'gender')
    #
    # def test_get_absolute_url(self):
    #     author = Author.objects.get(id=1)
    #     print(author.get_absolute_url())
    #     # self.assertEquals(author.get_absolute_url(), '/news/authors_name/1')
