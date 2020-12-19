from django.shortcuts import render,redirect
from . import models


def goods_detail(request):
    good_name = request.GET.get('good_name')
    print(good_name)
    if good_name:
        good = models.GoodInfo.objects.get(name=good_name)
        return render(request, 'z_goods/goodsdetail.html', locals())
    return render(request, 'z_user/home.html', locals())


