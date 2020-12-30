from django import template
import time

# 创建模板库的实例
register = template.Library()


# 注册过滤器
@register.filter(name="dealwithtime")
def dealwithtime(t1):
    if t1 < 1000000000000:
        x = time.localtime(t1)
        t2 = time.strftime('%Y-%m-%d %H:%M:%S', x).format(Y='年', m='月', d='日')
        return t2
    else:
        x = time.localtime(t1 / 1000)
        t2 = time.strftime('%Y-%m-%d %H:%M:%S', x).format(Y='年', m='月', d='日')
        return t2


@register.filter(name="isp2")
def isp2(acno):
    return '_' in acno


@register.filter(name="makeurl")
def makeurl(sstr):
    linkid = ''
    try:
        linkid = str(sstr)
    except:
        pass
    if '.' in linkid:
        return 'http://{}'.format(linkid)
    elif 'ac' in linkid:
        return 'https://www.acfun.cn/v/{}'.format(linkid)
    else:
        return 'https://www.bilibili.com/video/av{}'.format(linkid)


@register.filter(name="twpic")
def twpic(sstr: str):
    res = []
    if '@' in sstr:
        pics = sstr.split('@')
        for pic in pics:
            if pic != '':
                res.append(pic)
    return res


@register.filter(name="formatTimeFromYoutube")
def formatTimeFromYoutube(st):
    res_time = '{}-{}-{} {}:{}:{}'.format(st[:4], st[4:6], st[6:8], st[8:10], st[10:12], st[12:14])
    return res_time


@register.filter(name="ToStr")
def ToStr(sword):
    return str(sword)