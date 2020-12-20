from django.shortcuts import render, redirect
from z_goods.models import GoodInfo
from . import views
from . import models


# Create your views here.


def order(request):
    pass
    return render(request, 'z_order/order.html', locals())

def showorder(request):
    pass
    return render(request, 'z_order/showorder.html', locals())





# def cart(request):
#     if not request.session.get('is_login', None):
#         return redirect('/login/')
#     user = models.UserInfo.objects.get(username=request.session['user_name'])
#     cart_of_good = models.CartInfo.objects.filter(user=user)
#     if cart_of_good:
#         goods_in_cart = user.cartinfo_set.all()
#         lis = goods_in_cart
#     else:
#         return render(request, 'z_cart/cartemty.html', locals())
#     return render(request, 'z_cart/cart.html', locals())
