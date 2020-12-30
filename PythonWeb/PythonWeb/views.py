from django.http import HttpResponse
from django.shortcuts import render
from twitter.models import Tweets
from acfun.models import Acfun
from login.models import User
from login.models import Other
from bili.models import Bili
from youtube.models import Youtube
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
import time


def format_set(query_set_list: list):
    res = []
    for i in query_set_list:
        imgList = []
        imgLink = i['imgs']
        if '@' in imgLink:
            # imgLink = imgLink.split('@')[0]
            imgList.clear()
            for img in imgLink.split('@'):
                if img != '':
                    imgList.append(img)
        else:
            imgLink = '#'
            imgList.clear()
        res.append((i['text'], i['twer_id'], i['username'], i['createtime'], imgLink, imgList))
    return res


def YtbTime2TimeStamp(st):
    res_time = '{}-{}-{} {}:{}:{}'.format(st[:4], st[4:6], st[6:8], st[8:10], st[10:12], st[12:14])
    ts = time.mktime(time.strptime(res_time, '%Y-%m-%d %H:%M:%S'))
    return int(ts)


def add_set(query_set_ac: list, query_set_bi: list, query_set_ytb: list):
    res_ac = []
    res_bi = []
    res_ytb = []
    # res_tw = []
    for i in query_set_ac:
        ac_time = int(i['uploadtime'] / 1000)
        res_ac.append({'link': i['acno'], 'name': i['acname'], 'title': i['title'], 'uploadtime': ac_time,
                       'cover': i['cover'], 'type': 'acfun'})
    for i in query_set_bi:
        res_ac.append({'link': i['aid'], 'uploadtime': i['created'], 'title': i['title'],
                       'cover': i['pic'], 'name': i['author'], 'type': 'bili'})
    for i in query_set_ytb:
        ytb_time = YtbTime2TimeStamp(i['uploadtime'])
        res_ytb.append({'link': i['video'], 'uploadtime': ytb_time, 'title': i['title'],
                        'cover': i['cover'], 'name': i['channeltitle'], 'type': 'youtube'})
    return res_ac + res_bi + res_ytb


def add_set_tw(query_set_s: list, query_set_tw: list):
    res_s = []
    res_tw = []
    # res_tw = []
    for i in query_set_s:
        res_s.append({'link': i['link'], 'name': i['name'], 'title': i['title'], 'uploadtime': i['uploadtime'],
                      'cover': i['cover'], 'type': i['type']})
    for i in query_set_tw:
        tw_time = int(time.mktime(time.strptime(i['createtime'].split('.')[0], "%Y-%m-%dT%H:%M:%S")))
        res_tw.append({'link': i['fuk_id'], 'uploadtime': tw_time, 'title': i['text'],
                       'cover': i['imgs'], 'name': i['username'], 'type': 'twitter'})
    return res_s + res_tw


def index(request):
    return render(request, "index.html", {})


def about(request):
    tweets_count = len(Tweets.objects.using('twitterdb').all().values('fuk_id'))
    acfun_count = len(Acfun.objects.all().values('acno'))
    bili_count = len(Bili.objects.all().values('aid'))
    youtube_count = len(Youtube.objects.all().values('videoid'))
    user_count = len(User.objects.all())
    register_left_count = Other.objects.filter(name='register').values('left_count')[0]['left_count']
    return render(request, "about.html", {'tw_count': tweets_count,
                                          'ac_count': acfun_count,
                                          'bi_count': bili_count,
                                          'ytb_count': youtube_count,
                                          'user_count': user_count,
                                          'left_user_count': register_left_count,
                                          })


def search(request):
    is_login = None
    try:
        is_login = request.session['is_login']
    except:
        pass
    if not is_login:
        return render(request, "result.html", {})
    if request.method == "POST":
        keyword = request.POST.get('search', '')
        request.session['keyword'] = keyword
        print(keyword)
    if request.method == "GET":
        # keyword = request.POST.get('search', '')
        keyword = request.session['keyword']
        # print(keyword)
    if request.session['user_level'] > 4:
        res_tw = Tweets.objects.using('twitterdb').all().values('fuk_id', 'text', 'twer_id', 'username', 'createtime',
                                                                'imgs', 'video').filter(
            Q(text__icontains=keyword) | Q(username__icontains=keyword))
        # print(len(res_tw))
    res_bi = Bili.objects.all().values('aid', 'created', 'title', 'pic',
                                       'mid', 'author').order_by('-created').filter(
        Q(title__icontains=keyword) | Q(author__icontains=keyword))
    res_ac = Acfun.objects.all().values('acno', 'acerid', 'acname', 'uploadtime', 'title',
                                        'uploadtime', 'cover').filter(
        Q(title__icontains=keyword) | Q(acname__icontains=keyword))
    res_ytb = Youtube.objects.all().values('title', 'channeltitle', 'video', 'uploadtime',
                                           'cover').filter(
        Q(title__icontains=keyword) | Q(channeltitle__icontains=keyword))
    res = add_set(res_ac, res_bi, res_ytb)
    try:
        res = add_set_tw(res, res_tw)
    except Exception as e:
        print(e)
        pass
    # print(res)
    res = sorted(res, key=lambda value: value['uploadtime'], reverse=True)

    paginator = Paginator(res, 20)
    pages = paginator.page(1)
    res_page = 1
    page = '1'
    # print(paginator.page(1).object_list)
    fin_res = []
    fin_res = paginator.page(page).object_list
    pages = paginator.page(page)
    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        if page is None:
            res_page = 1
        else:
            res_page = int(page)
        try:
            fin_res = paginator.page(page).object_list
            pages = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            fin_res = paginator.page(1).object_list
            pages = paginator.page(1)
            res_page = 1

        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            fin_res = paginator.page(paginator.num_pages).object_list
            pages = paginator.page(paginator.num_pages)

    return render(request, "result.html",
                  {'data': fin_res, "pages": pages, "current_page": res_page, "res_count": len(res)})


def twittertools(request):
    pass
    return render(request, "abc.html", {})


def acfuntools(request):
    pass
    return render(request, "abc.html", {})


def bilitools(request):
    pass
    return render(request, "abc.html", {})


def weblog(request):
    return render(request, "weblog.html", {})
