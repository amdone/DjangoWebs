from django.http import HttpResponse
from django.shortcuts import render
from PythonWeb.models import Tweets
from acfun.models import Acfun
from login.models import User
from login.models import Other
from bili.models import Bili
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage


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


def index(request):
    return render(request, "index.html", {})


def twitter(request):
    is_login = None
    try:
        is_login = request.session['is_login']
    except:
        pass
    if not is_login:
        return render(request, "twitter.html", {})
    elif request.session['user_level'] < 5:
        return render(request, "twitter.html", {})

    # user_list = models.UserDetails.objects.all().values('user_name','user_password')
    tweets = Tweets.objects.using('twitterdb').all().values('text', 'twer_id', 'username', 'createtime', 'imgs').order_by('-createtime')

    paginator = Paginator(tweets, 10)
    res = []

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        if page is None:
            res_page = 1
        else:
            res_page = int(page)
        try:
            res = format_set(paginator.page(page).object_list)
            pages = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            res = format_set(paginator.page(1).object_list)
            pages = paginator.page(1)
            res_page = 1

        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            res = format_set(paginator.page(paginator.num_pages).object_list)
            pages = paginator.page(paginator.num_pages)

    # count = 25
    # res = []
    # for i in tweets:
    #     imgList = []
    #     imgLink = i['imgs']
    #     if '@' in imgLink:
    #         # imgLink = imgLink.split('@')[0]
    #         imgList.clear()
    #         for img in imgLink.split('@'):
    #             if img != '':
    #                 imgList.append(img)
    #     else:
    #         imgLink = '#'
    #         imgList.clear()
    #     res.append((i['text'], i['twer_id'], i['username'], i['createtime'], imgLink, imgList))
    #     count -= 1
    #     if count < 1:
    #         break
    return render(request, "twitter.html", {"data": res, "pages": pages, "current_page": res_page})


def about(request):
    tweets_count = len(Tweets.objects.using('twitterdb').all().values('fuk_id'))
    acfun_count = len(Acfun.objects.all().values('acno'))
    bili_count = len(Bili.objects.all().values('aid'))
    user_count = len(User.objects.all())
    register_left_count = Other.objects.filter(name='register').values('left_count')[0]['left_count']
    return render(request, "about.html", {'tw_count': tweets_count,
                                          'ac_count': acfun_count,
                                          'bi_count': bili_count,
                                          'user_count': user_count,
                                          'left_user_count': register_left_count,
                                          })


def twittertools(request):
    pass
    return render(request, "abc.html", {})


def acfuntools(request):
    pass
    return render(request, "abc.html", {})


def bilitools(request):
    pass
    return render(request, "abc.html", {})
