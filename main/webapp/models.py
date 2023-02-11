from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
STATUS = [('On_moderated', 'На модерации'), ('Published', 'Опубликовано'), ('On_deleted', 'На удалении'), ('Rejected', 'Отклоненые')]


class Adds(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='uploads/user_adds_image', verbose_name='Картинки')
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description_adds = models.TextField(max_length=300, null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='adds', verbose_name='Автор объявления')
    category = models.ForeignKey('webapp.Category', on_delete=models.PROTECT, verbose_name="Категория", related_name="category")
    price = models.IntegerField(verbose_name='Цена')
    status = models.CharField(max_length=50, default=STATUS[0][0], choices=STATUS, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    date_of_publication = models.DateTimeField(auto_now=False, verbose_name='Дата публикации', blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')


    def __str__(self):
        return f'{self.title}, {self.author}'



class Category(models.Model):
    name_category = models.CharField(max_length=50, verbose_name='category_name')
    def __str__(self):
        return f'{self.name_category}'

class Comments(models.Model):
    description_comment = models.TextField(max_length=2000, verbose_name='Комментарий')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comment', verbose_name='Автор комментария')
    adds = models.ForeignKey('webapp.Adds', on_delete=models.CASCADE, related_name='comments', verbose_name='Объявления')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание комментария')

    class Meta:
        permissions = [("view_not_moderated_review", "Видеть не модерированые отзывы")]

    def __str__(self):
        return f'{self.author.username} - {self.adds.title}'
