from django.contrib import admin
from .models import Bili


# Register your models here.

@admin.register(Bili)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['author', 'title']
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('aid', 'title', 'author', 'description', 'created')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-created',)

    # list_editable 设置默认可编辑字段，在列表里就可以编辑
    # list_editable = ['title', 'acname']

    # fk_fields 设置显示外键字段
    # fk_fields = ['category']
