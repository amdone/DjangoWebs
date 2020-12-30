from django.http import HttpResponse
from django.shortcuts import render, redirect
from login import models
from .forms import UserForm, RegisterForm
import datetime


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查内容是否正确！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                if '@' in username:
                    user = models.User.objects.get(email=username)
                else:
                    user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['user_level'] = user.level
                    request.session['user_exp'] = user.exp
                    models.User.objects.filter(name=username).update(last_login_time=datetime.datetime.now())
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except Exception as e:
                print(e)
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    register_left_count = models.Other.objects.filter(name='register').values('left_count')[0]['left_count']
    print(register_left_count)
    if register_left_count < 1:
        register_form = RegisterForm(request.POST)
        message = "暂无注册名额！"
    elif request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.c_time = datetime.datetime.now()
                new_user.save()
                register_left_count -= 1
                models.Other.objects.filter(name='register').update(left_count=register_left_count)
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")


def profile(request):
    pass
    return render(request, 'login/profile.html', {'msg_type': 'active1'})


def upgrade(request):
    if request.method == "POST":
        up_code = request.POST.get('up_code', '')
        s_code = {}
        try:
            s_code = \
                models.Exp.objects.all().values('id', 'code', 'add', 'usage', 'deadtime', 'type').filter(code=up_code)[
                    0]
        except:
            pass
        # print(s_code)
        if not s_code:
            message = "请检查升级码是否正确！"
            return render(request, 'login/profile.html', {'message': message, 'msg_type': 'active3'})
        else:
            if s_code['type'] == 'level':
                if s_code['add'] <= request.session['user_level']:
                    message = "您的级别已经比这个升级码还要高，无法升级！"
                    return render(request, 'login/profile.html', {'message': message, 'msg_type': 'active3'})
                elif s_code['deadtime']:
                    time_now = datetime.datetime.now()
                    if time_now.__gt__(s_code['deadtime']):
                        message = "该升级码已经过期！"
                        return render(request, 'login/profile.html', {'message': message, 'msg_type': 'active3'})
                else:
                    models.User.objects.filter(id=request.session['user_id']).update(level=s_code['add'])
                    models.Exp.objects.filter(code=up_code).update(usage=s_code['usage'] - 1)
                    request.session['user_level'] = s_code['add']
                    message = "升级成功！"
                    if s_code['usage'] - 1 < 1:
                        models.Exp.objects.filter(code=up_code).delete()
                    return render(request, 'login/profile.html',
                                  {'message': message, 'msg_type': 'active3', 'msg_ok': True})
    return render(request, 'login/profile.html')
