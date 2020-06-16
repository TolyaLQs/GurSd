from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from news.forms import NewCommentForm, ComplaintForm, ComplaintGCForm
from news.models import New, NewComment


def news_all(request):
    new = New.objects.all()
    print('1')
    context = {
        'new': new,
    }
    return render(request, 'news/news-site.html', context)


def news_game(request):
    new = New.objects.filter()
    context = {
        'new': new,
    }
    return render(request, 'news/game-news-site.html', context)


def news_developers(request):
    new = New.objects.filter()
    print('2')
    context = {
        'new': new,
    }
    return render(request, 'news/developers-news-site.html', context)


def new(request, n=None):
    if request.method == 'GET':
        if n:
            new = New.objects.filter(id=n)
            comment = NewComment.objects.filter(new_name=n)
            context = {
                'new': new,
                'comment': comment,
                'n': n,
            }
            return render(request, 'news/full-information-page-news.html', context)

    if request.method == 'POST':
        if 'text' in request.POST and request.POST['text']:
            add_comment = NewCommentForm(request.POST, request.FILES)
            if add_comment.is_valid():
                add_comment.save()
                comment = NewComment.objects.filter(new_name=n)
                i = 0
                for comm in comment:
                    i = comm.id
                return HttpResponseRedirect(f'/news/new/{n}/#id_comm{i}')
                # йцу
                # if n:
                #     new = New.objects.filter(id=n)
                #     comment = NewComment.objects.filter(new_name=n)
                #     context = {
                #         'new': new,
                #         'comment': comment,
                #         'n': n,
                #     }
                #     return render(request, 'news/full-information-page-news.html', context)

    if 'complaint_quantity' in request.POST and request.POST['complaint_quantity']:
        id = request.POST['comment']
        complaint_quanti = NewComment.objects.filter(id=id).first()
        add_complaint = ComplaintForm(request.POST, request.FILES, instance=complaint_quanti)
        if add_complaint.is_valid():
            complax = ComplaintGCForm(request.POST, request.FILES)
            if complax.is_valid():
                complax.save()
                add_complaint.save()
                if n:
                    new = New.objects.filter(id=n)
                    comment = NewComment.objects.filter(new_name=n)
                    context = {
                        'new': new,
                        'comment': comment,
                        'n': n,
                    }
                    return render(request, 'news/full-information-page-news.html', context)
    else:
        if n:
            new = New.objects.filter(id=n)
            comment = NewComment.objects.filter(new_name=n)
            context = {
                'new': new,
                'comment': comment,
                'n': n,
            }
            return render(request, 'news/full-information-page-news.html', context)

# Create your views here.
