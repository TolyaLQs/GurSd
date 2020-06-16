from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.shortcuts import render
from django.http import JsonResponse
from django.template.context_processors import csrf

from mainapp.forms import GameCommentForm, ComplaintForm, ComplaintGCForm
from mainapp.models import Game, Genre, GameComment, ComplaintGCG
from django.template.loader import render_to_string
from user.models import User
from django.contrib.auth import authenticate, login, logout
from user.forms import MyUserCreationForm, MyUserChangeForm
from django.core.mail import send_mail
from mainapp.models import Tag


def index(request, ):
    games = Game.objects.all()
    top = Game.objects.all().order_by('-rating')
    genre = Genre.objects.all()
    tags = Tag.objects.all()
    # tag_g = tags.tag_game_set.all()
    # print(tag_g)
    # tegs = Teg.objects.all()
    # tegs_game = TegGame.objects.all()
    # i=0
    # for t in tegs:
    #     i = i+1
    #     t.name_teg
    #     tegs_game = TegGame.objects.filter(teg_game=t.id)
    #     print(tegs_game.count(), i)
            # for t in tegs:
            #     i = 0
            #     print(t.name_teg)
            #     id = t.id
            #     # tegs_game = TegGame.objects.filter(teg_game=id).count()
            #     # col_tegs_game = tegs_game.count()

    context = {
        'games': games,
        'top': top,
        'genre': genre,
        'tags': tags,
        # 'tags_h': tags_h,
        # 'tegs_game': tegs_game,
    }
    return render(request, 'mainapp/index.html', context)


def android(request):
    games = Game.objects.filter(android=True)
    print(games)
    top = Game.objects.filter(android=True).order_by('-rating')
    genre = Genre.objects.all()
    context = {
        'games': games,
        'top': top,
        'genre': genre,
    }
    return render(request, 'mainapp/android.html', context)


def ios(request):
    games = Game.objects.filter(ios=True)
    top = Game.objects.filter(ios=True).order_by('-rating')
    genre = Genre.objects.all()
    context = {
        'games': games,
        'top': top,
        'genre': genre,
    }
    return render(request, 'mainapp/ios.html', context)


def windows(request):
    games = Game.objects.filter(windows=True)
    top = Game.objects.filter(windows=True).order_by('-rating')
    genre = Genre.objects.all()
    context = {
        'games': games,
        'top': top,
        'genre': genre,
    }
    return render(request, 'mainapp/windows.html', context)


def psp(request):
    games = Game.objects.filter(psp=True)
    top = Game.objects.filter(psp=True).order_by('-rating')
    genre = Genre.objects.all()
    context = {
        'games': games,
        'top': top,
        'genre': genre,
    }
    return render(request, 'mainapp/psp.html', context)


def xbox(request):
    games = Game.objects.filter(xbox=True)
    top = Game.objects.filter(xbox=True).order_by('-rating')
    genre = Genre.objects.all()
    context = {
        'games': games,
        'top': top,
        'genre': genre,
    }
    return render(request, 'mainapp/x-box.html', context)


def game(request, name=None):
    if request.method == 'GET':
        if name:
            print(name)
            games = Game.objects.filter(name=name)
            comment = GameComment.objects.filter(game_name=name)
            # complaintgsu = ComplaintGC.objects.filter(user_complaint=request.user)
            # print(complaintgsu)
            tags = Tag.objects.filter(tag_game__name=name)
            context = {
                'comment': comment,
                'games': games,
                'name': name,
                'tags': tags,
            }
            return render(request, 'mainapp/game.html', context)

    if request.method == 'POST':
        if 'text' in request.POST and request.POST['text']:
            add_comment = GameCommentForm(request.POST, request.FILES)
            if add_comment.is_valid():
                add_comment.save()
                comment = GameComment.objects.filter(game_name=name)
                i=0
                for comm in comment:
                    i = comm.id
                    print(i)
                return HttpResponseRedirect(f'/game/{name}/#id_comm{i}')
                # йцу
                # if name:
                #     print(name)
                #     games = Game.objects.filter(name=name)
                #     comment = GameComment.objects.filter(game_name=name)
                #     context = {
                #         'comment': comment,
                #         'games': games,
                #         'name': name,
                #     }
                #     return render(request, 'mainapp/game.html', context)

        if 'complaint_quantity' in request.POST and request.POST['complaint_quantity']:
            id = request.POST['comment']
            complaint_quanti = GameComment.objects.filter(id=id).first()
            add_complaint = ComplaintForm(request.POST, request.FILES, instance=complaint_quanti)
            if add_complaint.is_valid():
                complax = ComplaintGCForm(request.POST, request.FILES)
                if complax.is_valid():
                    complax.save()
                    add_complaint.save()
                    if name:
                        print(name)
                        games = Game.objects.filter(name=name)
                        comment = GameComment.objects.filter(game_name=name)
                        context = {
                            'comment': comment,
                            'games': games,
                            'name': name,
                        }
                        return render(request, 'mainapp/game.html', context)
        else:
            if name:
                print(name)
                games = Game.objects.filter(name=name)
                comment = GameComment.objects.filter(game_name=name)
                # complaintgsu = ComplaintGCG.objects.filter(user_complaint=request.user)
                # print(complaintgsu)
                tags = Tag.objects.filter(tag_game__name=name)
                context = {
                    'comment': comment,
                    'games': games,
                    'name': name,
                    'tags': tags,
                }
                return render(request, 'mainapp/game.html', context)


def ganre(request, gan):
    if request.method == 'GET':
        if gan:
            print(gan)
            games = Game.objects.filter(genre_name=gan)
            top = Game.objects.filter(genre_name=gan).order_by('-rating')
            genre = Genre.objects.all()
            ganr = Genre.objects.filter(name=gan)

    context = {
        'games': games,
        'top': top,
        'genre': genre,
        'ganr': ganr,
    }

    return render(request, 'mainapp/ganre.html', context)

