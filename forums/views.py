from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from user.forms import MyUserCreationForm, MyUserChangeForm
from forums.models import ForumsComment, ForumsRazdel, ForumsTema
from mainapp.models import Genre


def forums(request):
    forums_razdel = ForumsRazdel.objects.all().order_by('date_create')
    forums_tema = ForumsTema.objects.all().order_by('date_create')
    context = {
        'forums_razdel': forums_razdel,
        'forums_tema': forums_tema,
    }
    return render(request, 'forums/forum_start.html', context)


def forum(request, forum=None):
    if request.method == 'GET':
        if forum:
            forums_tema = ForumsTema.objects.filter(razdel=forum).order_by('date_create')
    context = {
        'forums_tema': forums_tema,
    }
    return render(request, 'forums/forum.html', context)


def categor_forum(request, categor=None, forum=None):
    if request.method == 'GET':
        if categor & forum:
            forums_tema = ForumsTema.objects.filter(razdel=categor, name=forum).order_by('date_create')

    context = {

    }
    return render(request, 'forums/forum_start.html', context)


def strims(request):
    context = {

    }
    return render(request, 'forums/forum_strim.html', context)


def strims_games(request):
    context = {

    }
    return render(request, 'forums/forum_games.html', context)


def strims_game_ganr(request):
    context = {

    }
    return render(request, 'forums/forum_game_ganr.html', context)


def video(request):
    context = {

    }
    return render(request, 'forums/forum_video.html', context)


def auth(request):
    context = {

    }
    return render(request, 'forums/auth.html', context)


def register(request):
    context = {

    }
    return render(request, 'forums/register.html', context)


def user_login(request):
    # if request.is_ajax():
    #     print('AJAX login', request.META['HTTP_REFERER'])
    #     context = {
    #         'login': reverse('auth:login'),
    #     }
    #     return JsonResponse(context)
    if request.POST:
        if 'email' in request.POST and request.POST['email']:
            email = request.POST['email']
            password = request.POST['psw']
            user = authenticate(email=email, password=password)
            if user is not None:
                print('пользователь найден: ', user)
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        elif 'fname' in request.POST and request.POST['fname']:
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            request.session['fname'] = first_name
            request.session['lname'] = last_name
            return HttpResponseRedirect(reverse('auth:register'))

    return render(request, 'authapp/login.html')


def user_logout(request):
    logout(request)     # стираем токен аутентификации из cookie
    return HttpResponseRedirect(reverse('index'))


def user_register(request):
    register_form = MyUserCreationForm()
    fname = request.session.get('fname', 'Нет имени')
    lname = request.session.get('lname', 'Нет фамилии')
    if request.method == "POST":
        register_form = MyUserCreationForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            email = request.POST['email']
            password = request.POST['password1']
            user = authenticate(email=email, password=password)
            if user is not None:
                print('пользователь найден: ', user)
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        register_form = MyUserCreationForm()
    context = {
        'register_form': register_form,
        'fname': fname,
        'lname': lname,
    }

    return render(request, 'authapp/register.html', context)