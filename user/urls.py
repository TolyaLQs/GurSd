from django.urls import re_path
import user.views as user

app_name = 'user' # ОБЯЗАТЕЛЬНО!!!

urlpatterns = [
    re_path('login/$', user.user_login, name='login'),
    re_path('logout/$', user.user_logout, name='logout'),
    re_path('register/$', user.user_register, name='register'),
    re_path('edit/$', user.user_edit, name='edit'),
    re_path('profile/(?P<id>.*\s*)/$', user.user_profile, name='profile'),
    re_path('message/$', user.user_message, name='message'),
    re_path('message/(?P<id>.*\s*)/$', user.user_message_id, name='message_id'),
]