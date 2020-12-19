from django.db import models

# Create your models here.

# 商品信息表


class GoodInfo(models.Model):
    state = (
        ("on", "在售"),
        ("out", "不售"),
    )

    name = models.CharField(max_length=50, unique=True, verbose_name="商品名称")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="商品价格")
    count = models.IntegerField(default=1, verbose_name="库存")
    detail = models.CharField(max_length=2000, verbose_name="商品详情", default="无")
    state = models.CharField(max_length=10, choices=state, default="在售", verbose_name="商品状态")
    picture = models.CharField(max_length=2083, verbose_name="商品图片", default="image_url")   # 商品图片url
    type = models.ForeignKey('GoodType', on_delete=models.CASCADE, verbose_name="类别")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"


# 商品种类表
class GoodType(models.Model):

    typename = models.CharField(max_length=10, unique=True, verbose_name="类别")

    def __str__(self):
        return self.typename

    class Meta:
        verbose_name = "商品类型"
        verbose_name_plural = "商品类型"
