from django.urls import re_path
import news.views as news

app_name = 'news'  # ОБЯЗАТЕЛЬНО!!!

urlpatterns = [
    re_path('news/$', news.news_all, name='news_all'),
    re_path('game/$', news.news_game, name='news_game'),
    re_path('developers/$', news.news_developers, name='news_developers'),
    re_path('new/(?P<n>.*\s*)/$', news.new, name='new'),
]
