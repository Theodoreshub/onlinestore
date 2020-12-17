from django.db import models
from django.core import validators

# Create your models here.


class UserInfo(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    username = models.CharField(max_length=128, verbose_name="用户名", unique=True)
    password = models.CharField(max_length=256, verbose_name="密码")
    email = models.EmailField(verbose_name="电子邮箱", unique=True)
    address = models.CharField(max_length=100, default="", verbose_name="地址", blank=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-created_time"]
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name



