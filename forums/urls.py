from django.urls import re_path
import forums.views as forums

app_name = 'forums'  # ОБЯЗАТЕЛЬНО!!!

urlpatterns = [
    re_path('forum/$', forums.forums, name='forums'),
    re_path('forums/(?P<forum>.*\s*)/$', forums.forum, name='forum'),
    re_path('foruma/(?P<forum>.+\s*)/$', forums.tema, name='categor_forum'),
]
