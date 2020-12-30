from django.contrib import admin
from .models import User, Other, Exp


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'name', 'sex', 'level', 'exp', 'last_login_time', 'c_time')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-c_time',)

    # list_editable 设置默认可编辑字段，在列表里就可以编辑
    list_editable = ['level', 'exp']

    list_display_links = ('id', 'name')

    # fk_fields 设置显示外键字段
    # fk_fields = ['category']


@admin.register(Exp)
class ExpAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'code', 'type', 'add', 'usage', 'deadtime')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)

    # list_editable 设置默认可编辑字段，在列表里就可以编辑
    list_editable = ['add', 'type', 'usage', 'deadtime']

    list_display_links = ('code', 'id')

    # fk_fields 设置显示外键字段
    # fk_fields = ['category']


@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'name', 'left_count', 'other')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)

    # list_editable 设置默认可编辑字段，在列表里就可以编辑
    list_editable = ['left_count', 'other']

    list_display_links = ('id', 'name')

    # fk_fields 设置显示外键字段
    # fk_fields = ['category']