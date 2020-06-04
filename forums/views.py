from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from forums.forms import ComplaintGCForm, ForumsCommentForm, ComplaintCommentForm
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
    return render(request, 'forums/index-forum-site.html', context)


def forum(request, forum=None):
    if request.method == 'GET':
        if forum:
            forums_tema = ForumsTema.objects.filter(razdel=forum).order_by('date_create')
    context = {
        'forums_tema': forums_tema,
    }
    return render(request, 'forums/create-new-theme.html', context)


def tema(request, categor=None, forum=None):
    if request.method == 'GET':
        if categor & forum:
            forums_tema = ForumsTema.objects.filter(razdel=categor, name=forum).order_by('date_create').first()
            comment = ForumsComment.objects.filter(forums=forum)

            context = {
                'comment': comment,
                'forums_tema': forums_tema,
                'forum': forum,
            }
            return render(request, 'forums/themes-post.html', context)

    if request.method == 'POST':
        if '' in request.POST and request.POST['']:
            add_comment = ForumsCommentForm(request.POST, request.FILES)
            if add_comment.is_valid():
                add_comment.save()
                if categor & forum:
                    forums_tema = ForumsTema.objects.filter(razdel=categor, name=forum).order_by('date_create').first()
                    comment = ForumsComment.objects.filter(forums=forum)
                    context = {
                        'comment': comment,
                        'forums_tema': forums_tema,
                    }
                    return render(request, 'forums/themes-post.html', context)

        if 'tema_complaint_quantity' in request.POST and request.POST['tema_complaint_quantity']:
            id = request.POST['comment']
            complaint_quanti = ForumsComment.objects.filter(id=id).first()
            add_complaint = ComplaintCommentForm(request.POST, request.FILES, instance=complaint_quanti)
            if add_complaint.is_valid():
                complax = ComplaintGCForm(request.POST, request.FILES)
                if complax.is_valid():
                    complax.save()
                    add_complaint.save()
                    if categor & forum:
                        forums_tema = ForumsTema.objects.filter(razdel=categor, name=forum).order_by(
                            'date_create').first()
                        comment = ForumsComment.objects.filter(forums=forum)
                        context = {
                            'comment': comment,
                            'forums_tema': forums_tema,
                        }
                        return render(request, 'forums/themes-post.html', context)