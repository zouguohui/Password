from django.contrib import admin
from .models import Type, Password

# Register your models here.
admin.site.site_header = '密码后台管理'
admin.site.site_title = '密码'


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    # 设置要显示在列表中的字段
    list_display = ('id', 'type1', 'type2')
    # 设置每页显示多少条记录
    list_per_page = 50
    # 排序方式
    ordering = ('id',)
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_bottom = True
    actions_on_top = True
    # 设置默认可编辑字段
    list_editable = ['type1', 'type2']


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'password', 'url', 'pid')
    list_per_page = 50
    actions_on_bottom = True
    actions_on_top = True
    ordering = ('id',)
    list_editable = ['title', 'user', 'password', 'url', 'pid']
