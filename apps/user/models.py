from django.db import models
from django.contrib.auth.models import AbstractUser

from models import SourceBaseModel, BaseModel


class Account(SourceBaseModel, AbstractUser):
    """用户表"""

    username = models.CharField(max_length=150, unique=True, verbose_name="登录名")
    name = models.CharField(verbose_name="姓名", max_length=10, db_index=True, null=True)

    class Meta:
        db_table = "user_accounts"
        verbose_name = "账号"
        verbose_name_plural = verbose_name
