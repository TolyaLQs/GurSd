"""kursach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.index, name='index'),
    path('android/', mainapp.android, name='android'),
    path('ios/', mainapp.ios, name='ios'),
    path('windows_phone', mainapp.windows, name='windows_phone'),
    path('psp/', mainapp.psp, name='psp'),
    path('xbox/', mainapp.xbox, name='xbox'),
    re_path('^game/(?P<name>.*\s*)/$', mainapp.game, name='game'),
    re_path('^ganre/(?P<gan>.*\s*)/$', mainapp.ganre, name='ganre'),
    re_path('^(?P<os>.*\s*)/ganre/(?P<gan>.*\s*)/$', mainapp.game, name='game'),
    re_path('^news/', include('news.urls', namespace='news')),
    re_path('^forums/', include('forums.urls', namespace='forums')),
    re_path('^auth/', include('user.urls', namespace='auth')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
