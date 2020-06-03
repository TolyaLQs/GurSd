from django.db import models
from user.models import User
# Create your models here.


class New(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128, unique=True)
    avatar = models.ImageField(verbose_name='Фото', upload_to='newsPhoto')
    desc = models.TextField(verbose_name='Описание', blank=True, max_length=2048)
    date = models.DateTimeField(verbose_name='Добавлена', auto_now_add=True)
    tems = ('игры', 'разработчики', 'другое')

    def __str__(self):
        return f'{self.date} {self.name}'

    class Meta:
        ordering = ['date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class NewComment(models.Model):
    new_name = models.ForeignKey(New, verbose_name='Название', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Коментарий', blank=True, max_length=548)
    date_added = models.DateTimeField(verbose_name='Добавлен комментария', auto_now_add=True)
    avatar = models.ImageField(verbose_name='Фото комментария', blank=True, upload_to='newCommentPhoto')
    moder_state = models.BooleanField(verbose_name='Проверил', blank=True, default=False)
    complaint_quantity = models.SmallIntegerField(verbose_name='кол-во жалоб', blank=True, default=0)

    def __str__(self):
        return f'{self.date_added} {self.author} {self.new_name}'

    class Meta:
        ordering = ['date_added']
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


class ComplaintGCN(models.Model):
    user_complaint = models.ForeignKey(User, verbose_name='Автор_ж_к_н', on_delete=models.CASCADE)
    comment = models.ForeignKey(NewComment, verbose_name='Коментарий', on_delete=models.CASCADE)