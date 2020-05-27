from django.urls import re_path
import forums.views as forums

app_name = 'forums'  # ОБЯЗАТЕЛЬНО!!!

urlpatterns = [
    re_path('', forums.forums, name='forums'),
    re_path('^(?P<forum>.*\s*)/$', forums.forum, name='forum'),
    re_path('^(?P<categor>.*\s*)/(?P<forum>.*\s*)/$', forums.categor_forum, name='categor_forum'),
    re_path('strims/', forums.strims, name='strims'),
    re_path('strims_games/', forums.strims_games, name='strims_games'),
    re_path('strims_game_ganr/', forums.strims_game_ganr, name='strims_game_ganr'),
    re_path('video/', forums.video, name='video'),
    re_path('auth/', forums.auth, name='auth'),
    re_path('register/', forums.register, name='register'),
]
