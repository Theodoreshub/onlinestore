from django.shortcuts import render,redirect
from . import models


def goods_detail(request):
    good_name = request.GET.get('good_name')
    good = models.GoodInfo.objects.get(name=good_name)
    return render(request, 'z_goods/goodsdetail.html', locals())


def search(request):
    words = request.POST.get('search_words')
    print(words)
    lis = models.GoodInfo.objects.filter(name__icontains=words)  # 以后再来把数据都加到详情里
    if lis:
        return render(request, 'z_goods/search.html', locals())
    return render(request, 'z_goods/searcherror.html', locals())

