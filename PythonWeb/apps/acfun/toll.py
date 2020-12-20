from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse


# 表单
def toll_form(request):
    return render(request, 'toll.html')


# 接收请求数据
def toll(request):
    request.encoding = 'utf-8'
    if 'tollCode' in request.GET and request.GET['tollCode']:
        if request.GET['tollCode'] == '123':
            message = '通过！: '
        else:
            message = '输入错误'
    else:
        message = '输入错误'
    return HttpResponse(message)


def toll2(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['tollCode']
    if ctx['rlt'] == '123':
        return redirect("/acfun/")
    else:
        ctx['rlt'] = '通行码错误'
        return render(request, "toll.html", ctx)
