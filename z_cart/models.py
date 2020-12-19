from django.db import models

from z_user.models import UserInfo
from z_goods.models import GoodInfo
# Create your models here.


class CartInfo(models.Model):

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey(GoodInfo, on_delete=models.CASCADE, verbose_name="商品")
    count = models.IntegerField(verbose_name="单个商品购买数量", default=0)
    added_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        ordering = ["-added_time"]
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username + '的购物车'
