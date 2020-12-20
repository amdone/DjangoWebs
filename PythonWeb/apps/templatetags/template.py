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
