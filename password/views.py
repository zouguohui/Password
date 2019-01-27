from django.shortcuts import render, redirect, reverse
from .models import Type, Password
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login.html')
def indexView(request):
    typelist = Type.objects.all()
    pwdlist = Password.objects.all()
    return render(request, 'index.html', locals())


# 用户登录
def loginView(request):
    # 设置标题和另外一个链接
    title = '登录'
    unit_1 = '/setpassword.html'
    unit_1_name = '修改密码'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                return redirect('/')
            else:
                tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在'
    return render(request, 'user.html', locals())


# 修改密码
def setpasswordView(request):
    title = '修改密码'
    unit_2 = '/login.html'
    unit_2_name = '立即登录'
    new_password = True
    if request.method == 'POST':
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=old_password)
            user.set_password(new_password)
            user.save()
            tips = '密码修改成功'
        else:
            tips = '用户不存在'
    return render(request, 'user.html', locals())


# 用户注销，退出登录
def logoutView(request):
    logout(request)
    return redirect('login.html')
