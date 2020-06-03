from django.urls import re_path
import forums.views as forums

app_name = 'forums'  # ОБЯЗАТЕЛЬНО!!!

urlpatterns = [
    re_path('', forums.forums, name='forums'),
    re_path('^(?P<forum>.*\s*)/$', forums.forum, name='forum'),
    re_path('^(?P<categor>.*\s*)/(?P<forum>.+\s*)/$', forums.tema, name='categor_forum'),
]
