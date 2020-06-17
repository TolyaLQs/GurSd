from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from user.forms import MyUserCreationForm, MyUserChangeForm, MyUserChangeAvatarForm
from user.models import User, UserFriend
from mainapp.models import UserGame
from django.http import JsonResponse


def user_login(request):
    if request.is_ajax():
        print('AJAX login', request.META['HTTP_REFERER'])
        context = {
            'login': reverse('auth:login'),
        }
        return JsonResponse(context)

    if request.POST:
        if 'email' in request.POST and request.POST['email']:
            email = request.POST['email']
            password = request.POST['psw']
            user = authenticate(email=email, password=password)
            if user is not None:
                print('пользователь найден: ', user)
                login(request, user)
                message = f'Пользователь с емайлом {email} залогинелся'
                send_mail(
                    'GurSdGames',
                    message,
                    'testyatesttest@yandex.ru',
                    [u'sdtolya@gmail.com'],
                )
                return HttpResponseRedirect(reverse('index'))
        elif 'fname' in request.POST and request.POST['fname']:
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            request.session['fname'] = first_name
            request.session['lname'] = last_name
            return HttpResponseRedirect(reverse('auth:register'))

    return render(request, 'authapp/login.html')


def user_logout(request):
    logout(request)  # стираем токен аутентификации из cookie
    return HttpResponseRedirect(reverse('auth:login'))


def user_register(request):
    register_form = MyUserCreationForm()
    fname = request.session.get('fname', 'Нет имени')
    lname = request.session.get('lname', 'Нет фамилии')
    if request.method == "POST":
        register_form = MyUserCreationForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            email = request.POST['email']
            message = f'Пользователь с емайлом {email} зарегистрировался'
            send_mail(
                'GurSdGames',
                message,
                'testyatesttest@yandex.ru',
                [u'sdtolya@gmail.com'],
            )
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


def user_edit(request):
    if request.method == "POST":
        edit_form = MyUserChangeForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))

    else:
        edit_form = MyUserChangeForm(instance=request.user)

    context = {
        'edit_form': edit_form
    }

    return render(request, 'authapp/edit.html', context)


def user_profile(request, id=None):
    game_quantity = 0
    friend_quantity = 0
    if request.method == 'GET':
        print(id)
        if id:
            profile = User.objects.filter(id=id)
            profile_friend = UserFriend.objects.filter(user_friend=id)
            print(profile_friend)
            profile_game = UserGame.objects.filter(user_game=id)
            for i in profile_game:
                game_quantity = game_quantity+1
            for u in profile_friend:
                friend_quantity = friend_quantity+1
            r = MyUserChangeAvatarForm(request.POST, request.FILES, instance=request.user)
            context = {
                'profile': profile,
                'profile_friend': profile_friend,
                'profile_game': profile_game,
                'game_quantity': game_quantity,
                'friend_quantity': friend_quantity,
                'r': r,
            }
            return render(request, 'authapp/user_profile.html', context)

    if request.method == "POST":
        print('1')
        if 'avatar' in request.POST and request.POST['avatar']:
            print('2')
            edit_for = MyUserChangeAvatarForm()
            print('3')
            if edit_for.is_valid():
                print('4')
                edit_for.save()
                print('5')
                return HttpResponseRedirect(f'/auth/profile/{id}')
    # else:
    #     print('6')
    #     if id:
    #         print('7')
    #         profile = User.objects.filter(id=id)
    #         profile_friend = UserFriend.objects.filter(user_friend=id)
    #         print(profile_friend)
    #         profile_game = UserGame.objects.filter(user_game=id)
    #         for i in profile_game:
    #             game_quantity = game_quantity+1
    #         for u in profile_friend:
    #             print(u.friend_user.first_name)
    #             friend_quantity = friend_quantity+1
    #         context = {
    #             'profile': profile,
    #             'profile_friend': profile_friend,
    #             'profile_game': profile_game,
    #             'game_quantity': game_quantity,
    #             'friend_quantity': friend_quantity,
    #         }
    #         return render(request, 'authapp/user_profile.html', context)

def user_message(request):
    pass


def user_message_id(request):
    pass

