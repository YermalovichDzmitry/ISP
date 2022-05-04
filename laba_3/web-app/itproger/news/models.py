from django.db import models
from django.urls import reverse


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Аннонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT,
                            null=True)  # Мы запретили удалять категории на котрые установленны ссылки в article

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
