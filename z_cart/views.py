from django.shortcuts import render, redirect
from z_goods.models import GoodInfo
from . import views
from . import models


# Create your views here.


def cart(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    user = models.UserInfo.objects.get(username=request.session['user_name'])
    cart_of_good = models.CartInfo.objects.filter(user=user)
    if cart_of_good:
        goods_in_cart = user.cartinfo_set.all()
        lis = goods_in_cart
    else:
        return render(request, 'z_cart/cartemty.html', locals())
    return render(request, 'z_cart/cart.html', locals())


def addgoods(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    good_name = request.GET.get('good_name')
    user = models.UserInfo.objects.get(username=request.session['user_name'])
    good = models.GoodInfo.objects.get(name=good_name)
    cart_of_good = models.CartInfo.objects.filter(user=user, goods=good)
    if cart_of_good:
        cart_of_good = models.CartInfo.objects.get(user=user, goods=good)
        cart_of_good.count = cart_of_good.count + 1
        cart_of_good.save()
    else:
        new_cart = models.CartInfo()
        new_cart.user = user
        new_cart.goods = good
        new_cart.count = 1
        new_cart.save()
    return render(request, 'z_goods/goodsdetail.html', locals())
