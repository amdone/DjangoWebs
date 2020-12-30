from django.shortcuts import render, redirect
from .models import Comments
import datetime


# Create your views here.
def level(request):
    return render(request, 'other/level.html', {})


def black(request):
    is_login = None
    try:
        is_login = request.session['is_login']
    except Exception as e:
        print(e)
    if not is_login:
        return render(request, "other/black.html", {})
    elif request.session['user_level'] < 5:
        return render(request, "other/black.html", {})
    return render(request, 'other/black.html', {})


def board(request):
    is_login = None
    try:
        is_login = request.session['is_login']
    except Exception as e:
        print(e)
    if not is_login:
        return render(request, "other/board.html", {})
    elif request.session['user_level'] > 0:
        res = Comments.objects.using('other_db').all().order_by('c_time')
        main_comments = []
        second_comments = {}
        for c in res:
            if c.to_id:
                # second_comments['{}'.format(c.to_id)] += [].append(c)
                second_comments.setdefault(str(c.to_id), [])
        for c in res:
            if c.to_id:
                second_comments[str(c.to_id)].append(
                    {'id': c.id, 'to_id': c.to_id, 'user_name': c.user_name, 'comment': c.comment,
                     'c_time': c.c_time})
                # second_comments.setdefault(str(c.to_id),
                #                            [].append({'id': c.id, 'user_name': c.user_name, 'comment': c.comment,
                #                                       'c_time': c.c_time}))
            else:
                main_comments.append(c)
        # print(second_comments)
        return render(request, "other/board.html", {'main': main_comments, 'second_dict': second_comments})
    return render(request, 'other/board.html', {})


def recomment(request):
    if request.method == "GET":
        if request.GET.get('mode') == 'add':
            return render(request, "other/add_comment.html", {'mode': 'add'})
            pass
        else:
            to_id = request.GET.get('to_id')
            if to_id is None:
                return render(request, "other/add_comment.html", {})
            else:
                try:
                    real_id = Comments.objects.get(id=to_id)
                    return render(request, "other/add_comment.html", {'to_id': to_id})
                except:
                    return render(request, "other/add_comment.html", {})
    if request.method == "POST":
        new_comment = Comments.objects.create()
        new_comment.comment = request.POST.get('text', '')
        new_comment.user_id = request.session['user_id']
        new_comment.user_name = request.session['user_name']
        new_comment.c_time = datetime.datetime.now()
        try:
            new_comment.to_id = request.POST.get('to_id', '')
        except:
            new_comment.to_id = 0
            pass
        new_comment.save()
        return redirect('/board/')
    return render(request, "other/add_comment.html", {})
