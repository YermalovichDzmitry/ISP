from django.db import models
from django.urls import reverse


class Address(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    genders = [("M", "Мужчина"), ("F", "Женщина")]
    gender = models.CharField(max_length=1, choices=genders, default="M")
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def get_absolute_url(self):
        return reverse('authors_name', kwargs={'authors_id': self.pk})


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Аннонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT,
                            null=True)  # Мы запретили удалять категории на котрые установленны ссылки в article
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):  # возвращает имя категории
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
