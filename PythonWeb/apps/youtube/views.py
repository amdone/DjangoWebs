from django.core.paginator import InvalidPage, EmptyPage, Paginator, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from youtube.models import Youtube


# Create your views here.
def youtube(request):
    is_login = None
    try:
        is_login = request.session['is_login']
    except:
        pass
    if not is_login:
        return render(request, "youtube.html", {})
    elif request.session['user_level'] < 0:
        return render(request, "youtube.html", {})
    # user_list = models.UserDetails.objects.all().values('user_name','user_password')
    youtubes = Youtube.objects.using('youtube_db').all().values('title', 'description', 'cover',
                                                                'uploadtime', 'channeltitle', 'video'
                                                                ).order_by('-uploadtime')
    paginator = Paginator(youtubes, 10)
    res = []

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        if page is None:
            res_page = 1
        else:
            res_page = int(page)
        try:
            res = paginator.page(page).object_list
            pages = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            res = paginator.page(1).object_list
            pages = paginator.page(1)
            res_page = 1

        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            res = paginator.page(paginator.num_pages).object_list
            pages = paginator.page(paginator.num_pages)
    return render(request, "youtube.html", {"data": res, "pages": pages, "current_page": res_page})
