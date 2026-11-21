from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '注册成功，请登录')
            return redirect('users:login')          # 注册成功 → 登录页
        # 不 valid：form.errors 里自动带"用户已存在""密码不一致"等，交给模板显示
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # 如果 @login_required 跳过来，next 会是 '/'
            return redirect(request.GET.get('next') or request.POST.get('next') or 'index')
        messages.error(request, '用户名或密码错误')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.info(request, '已退出登录')
    return redirect('users:login')               # 退出 → 登录页