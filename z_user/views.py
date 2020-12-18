from django.shortcuts import render, redirect
from . import models
from . import forms


# Create your views here.
def home(request):
    pass
    return render(request, 'z_user/home.html')


def login(request):
    if request.session.get('is_login', None):  #不允许重复登录
        return redirect('/home/')
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.UserInfo.objects.get(username=username)
            except:
                message = '用户不存在！'
                return render(request, 'z_user/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                return redirect('/home/')
            else:
                message = '密码不正确！'
                return render(request, 'z_user/login.html', locals())
        else:
            return render(request, 'z_user/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'z_user/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/home/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'z_user/register.html', locals())
            else:
                same_name_user = models.UserInfo.objects.filter(username=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'z_user/register.html', locals())
                same_email_user = models.UserInfo.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'z_user/register.html', locals())

                new_user = models.UserInfo()
                new_user.username = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'z_user/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'z_user/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/home/')
    request.session.flush()
    return redirect('/home/')
