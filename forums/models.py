from django.db import models
from user.models import User
from mainapp.models import Game, Genre


# Create your models here.
class ForumsRazdel(models.Model):
    name_game = models.ForeignKey(Game, verbose_name='Игра', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', max_length=16, unique=True)
    quantity_themes = models.SmallIntegerField(verbose_name='Количество тем', default=0)
    date_create = models.DateTimeField(verbose_name='Добавлена', auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['date_create']
        verbose_name = 'Раздел форума'
        verbose_name_plural = 'Разделы Форума'


class ForumsTema(models.Model):
    razdel = models.ForeignKey(ForumsRazdel, verbose_name='Раздел', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', max_length=16, unique=True)
    author = models.ForeignKey(User, to_field='email', verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст', max_length=2048)
    date_create = models.DateTimeField(verbose_name='Добавлена', auto_now_add=True)
    photo = models.ImageField(verbose_name='Фото', blank=True, upload_to='gamePhoto')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class ForumsComment(models.Model):
    forums = models.ForeignKey(ForumsTema, verbose_name='Название темы', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст', max_length=2048)
    date_create = models.DateTimeField(verbose_name='Добавлена', auto_now_add=True)

