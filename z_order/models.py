from django.db import models
from z_user.models import UserInfo
from z_goods.models import GoodInfo
# Create your models here.

class OrderList(models.Model):
    state = (
        ('on_the_road', '未收货'),
        ('get_it', '已收货'),
    )
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="对应用户")
    order_number = models.CharField(max_length=128, verbose_name="订单号", unique=False) # 要改
    added_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    address = models.CharField(max_length=128, verbose_name="配送地址")
    phone = models.CharField(max_length=128, verbose_name="收件电话")
    name = models.CharField(max_length=128, verbose_name="收件人")
    condition = models.CharField(max_length=32, choices=state, default="on_the_road")

    class Meta:
        ordering = ["-added_time"]
        verbose_name = "订单"
        verbose_name_plural = verbose_name


class OrderInfo(models.Model):
    order = models.ForeignKey(OrderList, on_delete=models.CASCADE, verbose_name="订单")
    goods = models.ForeignKey(GoodInfo, on_delete=models.CASCADE, verbose_name="商品")
    count = models.IntegerField(verbose_name="单个商品购买数量", default=0)

    class Meta:
        verbose_name = "订单详情"
        verbose_name_plural = verbose_name

