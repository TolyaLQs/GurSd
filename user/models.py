from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.utils.deconstruct import deconstructible



@deconstructible
class UnicodeEmailValidator(validators.RegexValidator):
    regex = r'^[\w.]+@[\w.]+\.[a-z]+$'
    message = 'Enter a valid email. This value may contain only letters,' \
              ' numbers, and @/./+/-/_ characters.'
    flags = 0


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email_validator = UnicodeEmailValidator()

    username = None
    email = models.EmailField(
        verbose_name='email address',
        max_length=50,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[email_validator],
        error_messages={
            'unique': "A user with that email already exists.",
        },
    )
    first_name = models.CharField(verbose_name='Имя', max_length=15, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=15, blank=True)
    avatar = models.ImageField(verbose_name='Аватарка', blank=True, default='users/ava.png', upload_to='users')
    age = models.SmallIntegerField(verbose_name='Возраст', blank=True, default=0)
    sex = models.TextField(verbose_name='Пол', blank=True)
    nickname = models.TextField(verbose_name='Никнейм', max_length=128)
    telephoneModel = models.TextField(verbose_name='Модель телефона', max_length=50)
    aboutMyself = models.TextField(verbose_name='О себе', max_length=250)
    contacts = models.TextField(verbose_name='Контакты', max_length=150)
    networksAndSites = models.TextField(verbose_name='Соцсети и сайты', max_length=100)
    favorites = models.TextField(verbose_name='Избранное', max_length=100)
    moderator = models.BooleanField(verbose_name='Модератор', default=False)


class UserFriend(models.Model):
    user_friend = models.ForeignKey(User, verbose_name='Пользаватель', on_delete=models.CASCADE)
    friend_user = models.ForeignKey(User, verbose_name='Друг', related_name='Друг', on_delete=models.CASCADE)



