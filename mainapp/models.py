from django.db import models
from django.utils.safestring import mark_safe

from user.models import User


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=16, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def was_published_recently(self):
        return Game.objects.filter(genre_name=self)


class Game(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128, unique=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='gamePhoto')
    genre_name = models.ForeignKey(Genre, to_field='name', verbose_name='Жанр', on_delete=models.CASCADE)
    video = models.ImageField(verbose_name='Видео', upload_to='gameVideo', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True, max_length=2048)

    android = models.BooleanField(verbose_name='Android', default=False)
    ios = models.BooleanField(verbose_name='IOS', default=False)
    windows = models.BooleanField(verbose_name='Windows', default=False)
    psp = models.BooleanField(verbose_name='PSP', default=False)
    xbox = models.BooleanField(verbose_name='X-Box', default=False)

    rating = models.SmallIntegerField(verbose_name='Рейтинг', default=0)
    added = models.DateTimeField(verbose_name='Добавлена', auto_now_add=True)
    language = models.BooleanField(verbose_name='Русский язык', default=False)
    paidContent = models.BooleanField(verbose_name='Платный контент', default=False)
    advertising = models.BooleanField(verbose_name='Реклама', default=False)
    active = models.BooleanField(verbose_name='active', default=False)

    def __str__(self):
        return f'{self.name}'

        # Here I return the avatar or picture with an owl, if the avatar is not selected

    def get_avatar(self):
        if not self.photo:
            return '/static/images/owl-gray.svg'
        return self.photo.url

        # method to create a fake table field in read only mode

    def avatar_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_avatar())

    def game_tag_colvo1(self):
        return Tag.objects.filter(tag_game=self)

    class Meta:
        ordering = ['added', 'name']
        verbose_name = 'Игру'
        verbose_name_plural = 'Игры'


class Requirement(models.Model):
    game_name = models.ForeignKey(Game, verbose_name='Название', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.game_name}'

    class Meta:
        ordering = ['game_name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class GamePhoto(models.Model):
    game = models.ForeignKey(Game, verbose_name='Название', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Фото', upload_to='gamePhoto')


class GameComment(models.Model):
    game_name = models.ForeignKey(Game, to_field='name', verbose_name='Название', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Коментарий', blank=True, max_length=548)
    date_added = models.DateTimeField(verbose_name='Добавлен комментария', auto_now_add=True)
    avatar = models.ImageField(verbose_name='Фото комментария', blank=True, upload_to='gameCommentPhoto')
    moder_state = models.BooleanField(verbose_name='Проверил', blank=True, default=False)
    complaint_quantity = models.SmallIntegerField(verbose_name='кол-во жалоб', blank=True, default=0)

    def __str__(self):
        return f'{self.date_added} {self.author} {self.game_name}'

    class Meta:
        ordering = ['date_added']
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


class ComplaintGCG(models.Model):
    user_complaint = models.ForeignKey(User, verbose_name='Автор жалобы', related_name='автор_ж_к_и', on_delete=models.CASCADE)
    comment = models.ForeignKey(GameComment, verbose_name='Коментарий', on_delete=models.CASCADE)


class UserGame(models.Model):
    user_game = models.ForeignKey(User, verbose_name='Пользаватель', on_delete=models.CASCADE)
    game_user = models.ForeignKey(Game, verbose_name='Название', on_delete=models.CASCADE)


class Tag(models.Model):
    name_tag = models.CharField(verbose_name='название тега', max_length=16, unique=True)
    tag_game = models.ManyToManyField(Game, verbose_name='игры')

    def __str__(self):
        return f'{self.name_tag}'

    def game_tag_colvo(self):
        return Tag.objects.filter(name_tag=self)

